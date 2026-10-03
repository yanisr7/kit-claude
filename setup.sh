#!/bin/bash
# Installation du kit Claude — à lancer une seule fois :  bash ~/kit-claude/setup.sh
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
VAULT="$HOME/Documents/Cerveau"
ok()   { printf "\033[32m✓\033[0m %s\n" "$1"; }
step() { printf "\n\033[1m▸ %s\033[0m\n" "$1"; }

[ "$(uname)" = "Darwin" ] || { echo "Ce kit est prévu pour macOS."; exit 1; }
[ "$(uname -m)" = "arm64" ] || echo "⚠️  Mac Intel détecté : tout marche sauf la transcription vidéo rapide (mlx-whisper)."

step "1/7 Homebrew"
if ! command -v brew >/dev/null; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv)"
  grep -q 'brew shellenv' ~/.zprofile 2>/dev/null || echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
fi
ok "brew"

step "2/7 Outils (node, python, ffmpeg, git)"
brew install node python ffmpeg git >/dev/null
ok "node $(node -v) · ffmpeg · git"

step "3/7 Claude Code"
if ! command -v claude >/dev/null; then
  curl -fsSL https://claude.ai/install.sh | bash
  export PATH="$HOME/.local/bin:$PATH"
  grep -q '.local/bin' ~/.zshrc 2>/dev/null || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
fi
ok "claude installé"

step "4/7 Profil Claude (CLAUDE.md + plugins de skills)"
mkdir -p ~/.claude
[ -f ~/.claude/CLAUDE.md ] && cp ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak
cp "$KIT/claude/CLAUDE.md" ~/.claude/CLAUDE.md
python3 - "$KIT/claude/settings.json" <<'PY'
import json, os, sys
p = os.path.expanduser("~/.claude/settings.json")
cur = json.load(open(p)) if os.path.exists(p) else {}
new = json.load(open(sys.argv[1]))
for k, v in new.items():
    cur[k] = {**cur.get(k, {}), **v} if isinstance(v, dict) else v
json.dump(cur, open(p, "w"), indent=2)
PY
for m in anthropics/claude-plugins-official anthropics/skills coreyhaines31/marketingskills; do
  claude plugin marketplace add "$m" >/dev/null 2>&1 || true
done
for p in superpowers@claude-plugins-official document-skills@anthropic-agent-skills example-skills@anthropic-agent-skills marketing-skills@marketingskills; do
  claude plugin install "$p" >/dev/null 2>&1 && ok "$p" || echo "  (à installer plus tard dans Claude : /plugin install $p)"
done

step "5/7 Cerveau Obsidian"
if [ ! -d "$VAULT" ]; then cp -R "$KIT/cerveau-modele" "$VAULT"; ok "vault créé : $VAULT"; else ok "vault déjà présent"; fi
brew list --cask obsidian >/dev/null 2>&1 || brew install --cask obsidian >/dev/null || true
claude mcp remove -s user obsidian >/dev/null 2>&1 || true
claude mcp add -s user obsidian -- npx -y mcp-obsidian "$VAULT" >/dev/null && ok "MCP obsidian"

step "6/7 Recherche X + Apify"
(cd "$KIT/mcp/search-x" && npm install --silent >/dev/null)
echo "Clé xAI pour la recherche X (https://console.x.ai → API Keys). Entrée pour passer :"
read -r XAI
claude mcp remove -s user search-x >/dev/null 2>&1 || true
if [ -n "$XAI" ]; then
  claude mcp add -s user search-x -e XAI_API_KEY="$XAI" -- node "$KIT/mcp/search-x/index.js" >/dev/null && ok "MCP search-x"
else
  echo "  → plus tard : relance ce script, ou demande à Claude de configurer search-x"
fi
claude mcp remove -s user apify >/dev/null 2>&1 || true
claude mcp add -s user --transport http apify "https://mcp.apify.com/?tools=actors,docs,apify/instagram-scraper" >/dev/null && ok "MCP apify (connexion au 1er usage via /mcp)"

step "7/7 Outils vidéo (Whisper)"
python3 -m venv "$KIT/.venv"
"$KIT/.venv/bin/pip" install -q --upgrade pip
if [ "$(uname -m)" = "arm64" ]; then "$KIT/.venv/bin/pip" install -q mlx-whisper pillow; else "$KIT/.venv/bin/pip" install -q openai-whisper pillow; fi
ok "whisper prêt ($KIT/.venv)"

printf "\n\033[1m🎉 Terminé.\033[0m Ouvre un nouveau terminal et tape :  claude\n"
echo "Puis lis GUIDE.md (ou demande à Claude : « lis ~/kit-claude/GUIDE.md et fais-moi le premier exercice »)."
