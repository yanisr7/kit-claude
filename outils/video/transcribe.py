# Transcrit des rushs avec Whisper (timestamps au mot) → un <rush>.json à côté du script de montage.
# Usage :  ~/kit-claude/.venv/bin/python ~/kit-claude/outils/video/transcribe.py "/chemin/rushs" [dossier_sortie]
import json, os, sys, glob

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(out, exist_ok=True)
try:
    import mlx_whisper
    run = lambda p: mlx_whisper.transcribe(p, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="fr", word_timestamps=True)
except ImportError:  # Mac Intel : whisper classique (plus lent)
    import whisper
    m = whisper.load_model("turbo")
    run = lambda p: m.transcribe(p, language="fr", word_timestamps=True)

for p in sorted(glob.glob(os.path.join(src, "*.mp4")) + glob.glob(os.path.join(src, "*.mov")) + glob.glob(os.path.join(src, "*.MOV")) + glob.glob(os.path.join(src, "*.MP4"))):
    name = os.path.splitext(os.path.basename(p))[0]
    dst = os.path.join(out, name + ".json")
    if os.path.exists(dst):
        print("déjà fait :", name); continue
    print("transcription :", name)
    r = run(p)
    json.dump({"segments": r["segments"]}, open(dst, "w"), ensure_ascii=False)
    # version lisible (pour que Claude choisisse les passages)
    with open(os.path.join(out, name + ".txt"), "w") as f:
        for s in r["segments"]:
            f.write(f"[{s['start']:7.1f} → {s['end']:7.1f}] {s['text'].strip()}\n")
print("ok")
