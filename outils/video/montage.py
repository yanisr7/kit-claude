# Montage automatique : liste de coupes (edit.py) → MP4 + XML Premiere éditable + plan HTML.
# Usage (dans le dossier du projet, qui contient edit.py et les .json de transcribe.py) :
#   ~/kit-claude/.venv/bin/python ~/kit-claude/outils/video/montage.py
#
# edit.py doit définir :
#   SRC  = "/chemin/des/rushs"
#   EDIT = [ ("nom_du_rush", debut_s, fin_s, "PARTIE", "ce qu'on entend"), ... ]
# Les coupes sont recalées sur les mots (Whisper) pour ne jamais couper au milieu d'un mot.
import json, os, sys, html, subprocess, urllib.parse
sys.path.insert(0, os.getcwd())
from edit import SRC, EDIT

PAD_IN, PAD_OUT = 0.10, 0.20     # marge avant / après la phrase
OUT_W, OUT_H, FPS = 1080, 1920, 25  # format de sortie (vertical réseaux sociaux)

def probe(path, entries, stream=True):
    a = ["ffprobe", "-v", "error"] + (["-select_streams", "v:0"] if stream else []) + ["-show_entries", entries, "-of", "csv=p=0", path]
    return subprocess.run(a, capture_output=True, text=True).stdout.strip()
def rush(name):
    for ext in (".mp4", ".MP4", ".mov", ".MOV"):
        if os.path.exists(os.path.join(SRC, name + ext)): return os.path.join(SRC, name + ext)
    sys.exit(f"Rush introuvable : {name}")

words, durs, dims = {}, {}, {}
for name in {e[0] for e in EDIT}:
    p = rush(name)
    durs[name] = float(probe(p, "format=duration", False))
    dims[name] = tuple(int(x) for x in probe(p, "stream=width,height").split(","))
    words[name] = [w for s in json.load(open(f"{name}.json"))["segments"] for w in s.get("words", [])] if os.path.exists(f"{name}.json") else []

cuts, t = [], 0.0
for name, a, b, part, label, *_ in EDIT:
    ws = [w for w in words[name] if (w["start"] + w["end"]) / 2 >= a and (w["start"] + w["end"]) / 2 <= b]
    if ws: a, b = ws[0]["start"], ws[-1]["end"]
    a, b = max(0, a - PAD_IN), min(durs[name], b + PAD_OUT)
    if cuts and cuts[-1]["name"] == name and a < cuts[-1]["b"]: a = cuts[-1]["b"]   # pas de mot répété
    cuts.append(dict(name=name, a=a, b=b, t=t, part=part, label=label)); t += b - a
print(f"{len(cuts)} coupes · durée {int(t//60)}:{int(t%60):02d}")

# 1) MP4
inputs = sorted({c["name"] for c in cuts}); idx = {n: i for i, n in enumerate(inputs)}
fc, cat = [], ""
for k, c in enumerate(cuts):
    i = idx[c["name"]]
    fc.append(f"[{i}:v]trim={c['a']:.3f}:{c['b']:.3f},setpts=PTS-STARTPTS,scale={OUT_W}:{OUT_H}:force_original_aspect_ratio=increase,crop={OUT_W}:{OUT_H},fps={FPS},setsar=1[v{k}]")
    fc.append(f"[{i}:a]atrim={c['a']:.3f}:{c['b']:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={c['b']-c['a']-0.03:.3f}:d=0.03[a{k}]")
    cat += f"[v{k}][a{k}]"
fc.append(f"{cat}concat=n={len(cuts)}:v=1:a=1[v][araw];[araw]loudnorm=I=-14:TP=-1.5:LRA=11[a]")
open("filtre.txt", "w").write(";\n".join(fc))
cmd = ["ffmpeg", "-y", "-v", "error", "-stats"]
for n in inputs: cmd += ["-i", rush(n)]
cmd += ["-filter_complex_script", "filtre.txt", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "montage.mp4"]
subprocess.run(cmd, check=True)

# 2) XML Premiere (Fichier > Importer) : chaque coupe reste modifiable
f = lambda s: round(s * FPS)
rate = f"<rate><timebase>{FPS}</timebase><ntsc>FALSE</ntsc></rate>"
seen = set()
def fileel(n):
    if n in seen: return f'<file id="f-{idx[n]}"/>'
    seen.add(n); w, h = dims[n]
    return (f'<file id="f-{idx[n]}"><name>{html.escape(os.path.basename(rush(n)))}</name><pathurl>file://{urllib.parse.quote(rush(n))}</pathurl>{rate}<duration>{f(durs[n])}</duration>'
            f'<media><video><samplecharacteristics>{rate}<width>{w}</width><height>{h}</height></samplecharacteristics></video>'
            f'<audio><samplecharacteristics><depth>16</depth><samplerate>48000</samplerate></samplecharacteristics><channelcount>2</channelcount></audio></media></file>')
def scale(n): return 100 * max(OUT_W / dims[n][0], OUT_H / dims[n][1])
v, a1, a2 = [], [], []
for k, c in enumerate(cuts):
    st, en, fin = f(c["t"]), f(c["t"]) + f(c["b"] - c["a"]), f(c["a"])
    ids = (f"v{k}", f"a{k}-1", f"a{k}-2")
    links = "".join(f"<link><linkclipref>{x}</linkclipref></link>" for x in ids)
    common = f'<name>{html.escape(c["part"] + " · " + c["label"][:40])}</name><enabled>TRUE</enabled><duration>{f(durs[c["name"]])}</duration>{rate}<start>{st}</start><end>{en}</end><in>{fin}</in><out>{fin + en - st}</out>'
    mot = (f'<filter><effect><name>Basic Motion</name><effectid>basic</effectid><effectcategory>motion</effectcategory><effecttype>motion</effecttype><mediatype>video</mediatype>'
           f'<parameter><parameterid>scale</parameterid><name>Scale</name><valuemin>0</valuemin><valuemax>1000</valuemax><value>{scale(c["name"]):.2f}</value></parameter></effect></filter>')
    v.append(f'<clipitem id="{ids[0]}">{common}{fileel(c["name"])}{mot}{links}</clipitem>')
    for cid, tr, lst in ((ids[1], 1, a1), (ids[2], 2, a2)):
        lst.append(f'<clipitem id="{cid}">{common}<file id="f-{idx[c["name"]]}"/><sourcetrack><mediatype>audio</mediatype><trackindex>{tr}</trackindex></sourcetrack>{links}</clipitem>')
trk = lambda x: "<track>" + "".join(x) + "</track>"
open("montage.xml", "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><sequence id="seq"><name>Montage IA (éditable)</name>'
    f'<duration>{f(t)}</duration>{rate}<media><video><format><samplecharacteristics>{rate}<width>{OUT_W}</width><height>{OUT_H}</height>'
    f'<pixelaspectratio>square</pixelaspectratio></samplecharacteristics></format>{trk(v)}</video>'
    f'<audio><numOutputChannels>2</numOutputChannels>{trk(a1)}{trk(a2)}</audio></media></sequence></xmeml>')

# 3) Plan de montage lisible
rows = "".join(f"<tr><td>{k+1}</td><td>{int(c['t']//60)}:{int(c['t']%60):02d}</td><td><b>{html.escape(c['part'])}</b></td><td>{html.escape(c['label'])}</td><td>{c['b']-c['a']:.1f}s</td></tr>" for k, c in enumerate(cuts))
open("plan.html", "w").write(f"<!doctype html><meta charset=utf-8><title>Plan de montage</title><style>body{{font-family:system-ui;max-width:900px;margin:30px auto;padding:0 16px}}td,th{{border-bottom:1px solid #ddd;padding:6px;text-align:left}}table{{border-collapse:collapse;width:100%}}</style><h1>Plan de montage</h1><p>{len(cuts)} coupes · {int(t//60)}:{int(t%60):02d}</p><table><tr><th>#</th><th>Temps</th><th>Partie</th><th>On entend</th><th>Durée</th></tr>{rows}</table>")
print("→ montage.mp4 · montage.xml (Premiere) · plan.html")
