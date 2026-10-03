# Installation du kit Claude sur Windows 10/11.
# A lancer dans PowerShell :
#   powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/yanisr7/kit-claude/main/install.ps1 | iex"
# (fichier volontairement sans accents : PowerShell 5 les lit mal)

$ErrorActionPreference = "Continue"
$KIT   = "$env:USERPROFILE\kit-claude"
$VAULT = "$env:USERPROFILE\Cerveau"
function Ok($m)   { Write-Host "  OK  $m" -ForegroundColor Green }
function Step($m) { Write-Host "`n>> $m" -ForegroundColor Cyan }
function RefreshPath { $env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User") + ";$env:USERPROFILE\.local\bin" }
function Winget($id) { winget install --id $id -e --silent --accept-package-agreements --accept-source-agreements | Out-Null }

if (Test-Path "$env:USERPROFILE\.claude\CLAUDE.md") {
  if (Select-String -Path "$env:USERPROFILE\.claude\CLAUDE.md" -Pattern "User Profile" -Quiet) { Write-Host "Config de Yanis detectee : installation annulee."; return }
}
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  Write-Host "winget manquant : installe 'App Installer' depuis le Microsoft Store puis relance." -ForegroundColor Red; return
}

Step "1/7 Outils : Git, Node, Python, ffmpeg, Obsidian (quelques minutes)"
foreach ($id in "Git.Git","OpenJS.NodeJS.LTS","Python.Python.3.12","Gyan.FFmpeg","Obsidian.Obsidian") { Winget $id; Ok $id }
RefreshPath

Step "2/7 Telechargement du kit"
if (Test-Path "$KIT\.git") { git -C $KIT pull -q } else { if (Test-Path $KIT) { Remove-Item -Recurse -Force $KIT }; git clone -q https://github.com/yanisr7/kit-claude.git $KIT }
Ok $KIT

Step "3/7 Claude Code"
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) { irm https://claude.ai/install.ps1 | iex; RefreshPath }
$userPath = [Environment]::GetEnvironmentVariable("Path","User")
if ($userPath -notlike "*\.local\bin*") { [Environment]::SetEnvironmentVariable("Path", "$userPath;$env:USERPROFILE\.local\bin", "User") }
Ok "claude"

Step "4/7 Profil Claude (CLAUDE.md + plugins de skills)"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude" | Out-Null
if (Test-Path "$env:USERPROFILE\.claude\CLAUDE.md") { Copy-Item "$env:USERPROFILE\.claude\CLAUDE.md" "$env:USERPROFILE\.claude\CLAUDE.md.bak" -Force }
Copy-Item "$KIT\claude\CLAUDE.md" "$env:USERPROFILE\.claude\CLAUDE.md" -Force
py -3 "$KIT\claude\merge_settings.py" "$KIT\claude\settings.json"
foreach ($m in "anthropics/claude-plugins-official","anthropics/skills","coreyhaines31/marketingskills") { claude plugin marketplace add $m 2>$null | Out-Null }
foreach ($p in "superpowers@claude-plugins-official","document-skills@anthropic-agent-skills","example-skills@anthropic-agent-skills","marketing-skills@marketingskills") {
  claude plugin install $p 2>$null | Out-Null
  if ($LASTEXITCODE -eq 0) { Ok $p } else { Write-Host "  (plus tard dans Claude : /plugin install $p)" }
}

Step "5/7 Cerveau Obsidian"
if (-not (Test-Path $VAULT)) { Copy-Item -Recurse "$KIT\cerveau-modele" $VAULT; Ok "vault cree : $VAULT" } else { Ok "vault deja present" }
claude mcp remove -s user obsidian 2>$null | Out-Null
claude mcp add -s user obsidian -- cmd /c npx -y mcp-obsidian "$VAULT" | Out-Null
Ok "MCP obsidian"

Step "6/7 Recherche X + Apify"
Push-Location "$KIT\mcp\search-x"; npm install --silent 2>$null | Out-Null; Pop-Location
$XAI = Read-Host "Cle xAI pour la recherche X (https://console.x.ai -> API Keys). Entree pour passer"
claude mcp remove -s user search-x 2>$null | Out-Null
if ($XAI) { claude mcp add -s user search-x -e "XAI_API_KEY=$XAI" -- node "$KIT\mcp\search-x\index.js" | Out-Null; Ok "MCP search-x" }
else { Write-Host "  -> plus tard : relance l'installation, ou demande a Claude de configurer search-x" }
claude mcp remove -s user apify 2>$null | Out-Null
claude mcp add -s user --transport http apify "https://mcp.apify.com/?tools=actors,docs,apify/instagram-scraper" | Out-Null
Ok "MCP apify (connexion au 1er usage via /mcp)"

Step "7/7 Outils video (Whisper)"
py -3 -m venv "$KIT\.venv"
& "$KIT\.venv\Scripts\python.exe" -m pip install -q --upgrade pip
& "$KIT\.venv\Scripts\python.exe" -m pip install -q faster-whisper pillow
Ok "whisper pret"

Write-Host "`nTermine. Ferme cette fenetre, ouvre un NOUVEAU PowerShell et tape :  claude" -ForegroundColor Green
Write-Host "Puis demande-lui : lis ~/kit-claude/GUIDE.md et fais-moi le premier exercice"
