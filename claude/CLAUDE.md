# Profil — comment je travaille avec Claude

J'apprends à piloter des projets (sites, Shopify, vidéos, présentations, recherche) avec Claude Code.
Je ne suis pas développeur : explique simplement quand c'est utile, sans jargon inutile.

## Cerveau — vault Obsidian

Toutes mes connaissances et le contexte de mes projets sont dans le vault Obsidian :

```
~/Documents/Cerveau/
├── Mes Projets/      ← un sous-dossier par projet
├── Idées/            ← réflexions et brainstorms
```

Chaque dossier projet contient (convention) :
- `Journal.md` — historique des sessions, prochaine étape
- `État Actuel.md` — photo du projet (stack, pages, derniers travaux)
- `Règles Métier.md` — les "pourquoi" que le code ne dit pas
- `Décisions.md` — choix importants et leurs raisons

Règles :
1. **Avant toute tâche sur un projet**, s'il a un dossier dans `Mes Projets/`, lire `Journal.md` et `État Actuel.md`.
2. **Nouveau projet** → créer son dossier en copiant `Mes Projets/_Modèle projet/`.
3. **Quand je dis "sauvegarde"** en fin de session :
   - `Journal.md` → toujours (résumé de la session + prochaine étape)
   - les autres fichiers → seulement si quelque chose d'important a changé.

## Façon de travailler

- **Analyse avant code** : proposer un plan court, attendre ma validation, puis faire.
- **Commit + push** après chaque phase de travail (GitHub).
- Réponses **courtes et concrètes**, en français. Pas de listes interminables quand 2 lignes suffisent.
- Quand tu as fini, dis-moi comment **vérifier** le résultat moi-même (lien, fichier à ouvrir…).
- Explique en une phrase le "pourquoi" de tes choix : je suis là pour apprendre.

## Règles de sécurité

- **Jamais inventer de données légales** (TVA, SIREN, IBAN, adresse) : demander ou laisser vide.
- **Jamais publier en live** (thème Shopify, site, post) sans ma confirmation explicite.
- Avant de modifier quelque chose de live : faire une **sauvegarde** d'abord.
- Ne jamais mettre de clé API / mot de passe dans un fichier envoyé sur GitHub (utiliser `.env`, ignoré par git).

## Outils

- **Recherche Twitter/X** : utiliser l'outil `search_x` (MCP search-x) pour toute veille ou recherche de tendances.
- **Obsidian** : MCP obsidian pour lire/chercher dans le cerveau.
- **Apify** : scraping Instagram (posts, commentaires, profils).
- **Recettes** de nos workflows (montage vidéo, Shopify, présentations, veille X) : `~/kit-claude/recettes/`. Les lire avant de faire ce type de tâche.
- **Outils vidéo** : `~/kit-claude/outils/video/` (transcription Whisper + montage ffmpeg + XML Premiere).
