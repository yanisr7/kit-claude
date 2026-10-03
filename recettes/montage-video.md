# Recette — Montage vidéo avec Claude

**Principe :** Claude ne « regarde » pas la vidéo, il **lit ce qui est dit**. On transcrit les rushs (Whisper), Claude choisit les passages, un script coupe avec ffmpeg et sort un **XML Premiere** pour finir à la main.

> Claude = la structure (quoi garder, dans quel ordre). Premiere = les finitions (musique, étalonnage, effets).

## Étapes

1. **Ranger** : un dossier par vidéo, ex. `~/Videos/projet-x/`. Rushs dans un sous-dossier ou dans Téléchargements.
2. **Transcrire** (le plus simple : demander à Claude de le faire). Sur Windows, remplacer `.venv/bin/python` par `.venv\Scripts\python.exe` :
   ```
   ~/kit-claude/.venv/bin/python ~/kit-claude/outils/video/transcribe.py "/chemin/rushs" .
   ```
   → un `.json` (timing au mot) et un `.txt` lisible par rush.
3. **Brief à Claude** : *« Lis les .txt. Fais-moi un montage de 3 min : accroche forte, l'histoire, la chute. Propose-moi le plan avant. »*
4. Claude écrit `edit.py` (liste de coupes) → tu valides le plan.
5. **Rendu** :
   ```
   ~/kit-claude/.venv/bin/python ~/kit-claude/outils/video/montage.py
   ```
   → `montage.mp4` (à regarder), `montage.xml` (Premiere), `plan.html` (le plan lisible).
6. **Itérer** en langage naturel : *« coupe le "euh" à 1:12 », « mets la réaction avant l'explication », « plus court sur la partie technique »*. Claude modifie `edit.py`, on relance.
7. **Premiere** : Fichier → Importer → `montage.xml`. Chaque coupe reste modifiable. Si on change la structure → nouvel import (nouvelle séquence).

## Ce que Claude peut ajouter ensuite (demande-lui)
- Zooms alternés entre les plans (dynamisme), recadrage visage.
- Images en split-screen (moitié visuel / moitié vidéo) quand on parle d'un visuel.
- Cartons de chapitre, étiquettes, écran de fin (images PNG ou animations **Remotion**).
- **J-cut** : la voix d'un plan commence sur les images d'un autre.
- Fichier **SRT** de sous-titres.
- Son normalisé à -14 LUFS (déjà fait par défaut).

## Pièges connus
- Whisper se trompe sur les noms propres → corriger dans les sous-titres.
- Un mot peut « déborder » d'une coupe à l'autre → dire à Claude « j'entends "on" en trop au début » : il recale au mot près.
- Toujours **regarder le MP4** avant de dire que c'est bon.
