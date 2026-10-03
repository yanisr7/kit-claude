# Kit Claude — notre façon de bosser

Tout ce qu'il faut pour que ton Claude travaille comme le mien : la façon de travailler, les skills, la recherche sur X, le cerveau Obsidian et les outils de montage vidéo.

## Avant de commencer
- Un **PC Windows 10/11** ou un **Mac**.
- Un abonnement **Claude Pro ou Max** (claude.ai).
- Un compte **GitHub** (gratuit).
- *(Optionnel)* une clé **xAI** pour la recherche sur X : https://console.x.ai → API Keys (quelques € de crédit suffisent).
- *(Optionnel)* un compte **Apify** pour le scraping Instagram : https://apify.com.

## Installation sur Windows (10-15 min)
Menu Démarrer → tape **PowerShell** → ouvre-le, colle cette ligne, Entrée :

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/yanisr7/kit-claude/main/install.ps1 | iex"
```

Windows va demander plusieurs fois « Autoriser cette application à apporter des modifications ? » → **Oui**. À la fin, ferme PowerShell, rouvre-le et tape `claude`.

## Installation sur Mac (5-10 min)
Ouvre l'app **Terminal** et colle :

```bash
mkdir -p ~/kit-claude && curl -L https://github.com/yanisr7/kit-claude/archive/refs/heads/main.tar.gz | tar xz -C ~/kit-claude --strip-components 1 && bash ~/kit-claude/setup.sh
```

Le script installe Homebrew, Node, Python, ffmpeg, Claude Code, les plugins de skills, Obsidian et les outils vidéo, et il configure tout. Il te demandera ton mot de passe Mac (normal) et ta clé xAI (Entrée pour passer).

Ensuite :
1. Ouvre un **nouveau** terminal et tape `claude`. Connecte-toi avec ton compte Claude.
2. Dans Claude, tape `/mcp` pour vérifier que obsidian, search-x et apify sont là (Apify te demandera de te connecter au premier usage).
3. Ouvre **Obsidian** → « Ouvrir un dossier comme coffre » → le dossier `Cerveau` (dans ton dossier utilisateur : `C:\Users\TonNom\Cerveau` sur Windows).
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
Relancer la même commande d'installation (elle remplace les fichiers du kit, ton cerveau Obsidian n'est pas touché).
