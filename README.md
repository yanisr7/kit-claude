# Kit Claude — notre façon de bosser

Tout ce qu'il faut pour que ton Claude travaille comme le mien : la façon de travailler, les skills, la recherche sur X, le cerveau Obsidian et les outils de montage vidéo.

## Avant de commencer
- Un **Mac** (Apple Silicon M1/M2/M3/M4 de préférence).
- Un abonnement **Claude Pro ou Max** (claude.ai).
- Un compte **GitHub** (gratuit).
- *(Optionnel)* une clé **xAI** pour la recherche sur X : https://console.x.ai → API Keys (quelques € de crédit suffisent).
- *(Optionnel)* un compte **Apify** pour le scraping Instagram : https://apify.com.

## Installation (5-10 min)
Ouvre l'app **Terminal** et colle :

```bash
git clone https://github.com/yanisr7/kit-claude.git ~/kit-claude && bash ~/kit-claude/setup.sh
```

Le script installe Homebrew, Node, Python, ffmpeg, Claude Code, les plugins de skills, Obsidian et les outils vidéo, et il configure tout. Il te demandera ton mot de passe Mac (normal) et ta clé xAI (Entrée pour passer).

Ensuite :
1. Ouvre un **nouveau** terminal et tape `claude`. Connecte-toi avec ton compte Claude.
2. Dans Claude, tape `/mcp` pour vérifier que obsidian, search-x et apify sont là (Apify te demandera de te connecter au premier usage).
3. Ouvre **Obsidian** → « Ouvrir un dossier comme coffre » → `Documents/Cerveau`.
4. Lis **[GUIDE.md](GUIDE.md)** et fais les exercices.

## Contenu
| Dossier | Quoi |
|---|---|
| `claude/` | `CLAUDE.md` (la façon de travailler) + réglages plugins |
| `recettes/` | nos workflows pas à pas (vidéo, X, Shopify, présentations, Obsidian) |
| `outils/video/` | transcription Whisper + montage auto → MP4 + XML Premiere |
| `mcp/search-x/` | l'outil de recherche Twitter/X |
| `cerveau-modele/` | le modèle de vault Obsidian |

## Mettre à jour le kit
```bash
cd ~/kit-claude && git pull && bash setup.sh
```
