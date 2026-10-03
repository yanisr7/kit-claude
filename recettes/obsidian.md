# Recette — Le cerveau Obsidian

Claude **oublie tout** entre deux conversations. Le vault Obsidian (`~/Cerveau`) est sa mémoire longue : il le lit au début, il le met à jour à la fin.

## Routine
- **Début de session** : *« on bosse sur [projet] »* → Claude lit `Journal.md` + `État Actuel.md` du projet.
- **Fin de session** : *« sauvegarde »* → Claude écrit le résumé + la prochaine étape dans `Journal.md`.
- **Nouveau projet** : *« crée le dossier projet pour [nom] dans le cerveau »*.

## Les 4 fichiers par projet
| Fichier | Quand il change |
|---|---|
| `Journal.md` | à chaque session |
| `État Actuel.md` | quand le projet change de visage (nouvelle page, nouvel outil) |
| `Règles Métier.md` | quand tu expliques un « pourquoi » (ex. « le client veut toujours valider ») |
| `Décisions.md` | quand on tranche entre plusieurs options |

Ouvre le vault dans l'app Obsidian pour tout lire toi-même (Ouvrir un dossier → le dossier `Cerveau` de ton dossier utilisateur).

## Mémoire automatique de Claude
Quand tu dis *« retiens que… »*, Claude enregistre une préférence dans sa propre mémoire (`~/.claude/projects/.../memory/`). Utile pour les habitudes (« pour Twitter utilise toujours search_x »). Le contexte des projets, lui, va dans Obsidian.
