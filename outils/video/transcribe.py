# Transcrit des rushs avec Whisper (timestamps au mot) → un <rush>.json à côté du script de montage.
# Usage (Mac) :  ~/kit-claude/.venv/bin/python ~/kit-claude/outils/video/transcribe.py "/chemin/rushs" [dossier_sortie]
import json, os, sys, glob

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(out, exist_ok=True)
try:
    import mlx_whisper
    run = lambda p: mlx_whisper.transcribe(p, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", language="fr", word_timestamps=True)
except ImportError:  # Windows / Mac Intel : faster-whisper
    from faster_whisper import WhisperModel
    m = WhisperModel("large-v3-turbo", device="auto", compute_type="int8")
    def run(p):
        segs, _ = m.transcribe(p, language="fr", word_timestamps=True)
        return {"segments": [{"start": s.start, "end": s.end, "text": s.text,
                              "words": [{"word": w.word, "start": w.start, "end": w.end} for w in s.words]} for s in segs]}

for p in sorted({q for e in ("mp4", "mov", "MP4", "MOV") for q in glob.glob(os.path.join(src, "*." + e))}):
    name = os.path.splitext(os.path.basename(p))[0]
    dst = os.path.join(out, name + ".json")
    if os.path.exists(dst):
        print("déjà fait :", name); continue
    print("transcription :", name)
    r = run(p)
    json.dump({"segments": r["segments"]}, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
    # version lisible (pour que Claude choisisse les passages)
    with open(os.path.join(out, name + ".txt"), "w", encoding="utf-8") as f:
        for s in r["segments"]:
            f.write(f"[{s['start']:7.1f} → {s['end']:7.1f}] {s['text'].strip()}\n")
print("ok")
