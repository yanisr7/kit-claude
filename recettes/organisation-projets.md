# Organiser ses projets en fichiers .md (la mémoire de Claude)

## Pourquoi
Claude **oublie tout** d'une conversation à l'autre. Pour qu'il reprenne un projet là où on l'a laissé, on lui laisse des **notes écrites** (fichiers `.md`) dans le projet. Il les lit au début, il les met à jour à la fin.

Pas besoin d'Obsidian : ce sont de simples fichiers texte, rangés **directement dans le dossier du projet**. Bonus : ils sont sauvegardés sur GitHub avec le code.

## La structure

```
mon-projet/
├── CLAUDE.md              ← la consigne que Claude lit automatiquement en ouvrant le projet
├── docs/
│   ├── Journal.md         ← ce qu'on a fait, session par session + la prochaine étape
│   ├── Etat-Actuel.md     ← la photo du projet aujourd'hui
│   ├── Regles-Metier.md   ← les « pourquoi » que le code ne dit pas
│   ├── Decisions.md       ← les choix importants et leurs raisons
│   └── (notes en plus)    ← ex. Cadrage.md, Presentation-client.md, Idees.md…
└── … le reste du projet (code, images, vidéos)
```

> Évite les accents et les espaces dans les noms de fichiers : sur Windows et dans le terminal, c'est source de bugs.

## Les 4 fichiers, à quoi ils servent

### `Journal.md` — mis à jour à **chaque** session
L'historique, **le plus récent en haut**. C'est le fichier le plus important : c'est lui qui dit « où on en est ».

```markdown
# Journal — Mon projet

## 3 octobre 2026 — Page d'accueil + formulaire de contact
- Fait : section héros avec photo, grille des produits, formulaire de contact.
- Problème : le formulaire n'envoyait rien → corrigé (mauvaise adresse email).
- **Prochaine étape :** mettre le site en ligne sur Vercel.

## 1er octobre 2026 — Démarrage
- …
```

### `Etat-Actuel.md` — mis à jour quand le projet **change de visage**
Quelqu'un qui ne lit que ce fichier doit comprendre le projet en 1 minute.

```markdown
# État actuel — Mon projet
- **Objectif :** site vitrine pour ma marque de t-shirts.
- **Outils :** HTML/CSS, hébergé sur Vercel, code sur GitHub.
- **Liens :** site https://…  ·  repo https://github.com/…
- **Pages :** Accueil, Produits, Contact.
- **Ce qui reste :** page À propos, version anglaise.
```

### `Regles-Metier.md` — quand tu expliques un **« pourquoi »**
Ce que Claude ne peut pas deviner en lisant le code.

```markdown
# Règles métier
- La livraison est offerte dès 100 €.
- Le client veut TOUJOURS valider avant qu'on publie.
- Jamais de photos de mannequins, uniquement des produits portés en situation.
```

### `Decisions.md` — quand on **tranche** entre plusieurs options
Pour ne pas rediscuter 10 fois la même chose.

```markdown
# Décisions

## 3 octobre 2026 — Vercel plutôt que Netlify
- **Choix :** Vercel.
- **Pourquoi :** déploiement auto à chaque push GitHub, gratuit.
- **Écarté :** Netlify (marche aussi, mais on utilise déjà Vercel ailleurs).
```

### Notes en plus (libres)
Tout ce qui mérite sa propre page : un cadrage client, une stratégie de contenu, une liste d'idées, un compte rendu de réunion. Un sujet = un fichier.

## Le `CLAUDE.md` du projet (à copier-coller)
Claude lit **automatiquement** le fichier `CLAUDE.md` à la racine du projet. C'est lui qui dit à Claude d'utiliser les notes :

```markdown
# Mon projet

## Mémoire du projet
Les notes du projet sont dans `docs/` :
- Au **début** de chaque session : lire `docs/Journal.md` et `docs/Etat-Actuel.md`.
- Avant une décision importante : vérifier `docs/Regles-Metier.md` et `docs/Decisions.md`.
- Quand je dis **« sauvegarde »** :
  - `docs/Journal.md` → toujours (résumé de la session + prochaine étape, en haut du fichier)
  - les autres fichiers → seulement si quelque chose d'important a changé
  - puis commit + push sur GitHub.
```

## La routine
1. **Nouveau projet** → dis à Claude : *« crée la structure de notes (CLAUDE.md + docs/) pour ce projet »*.
2. **Début de session** → *« on reprend »* : Claude lit le Journal et te dit où on en était.
3. **Pendant** → quand tu expliques un pourquoi ou que tu tranches un choix : *« note-le dans les règles métier / les décisions »*.
4. **Fin de session** → *« sauvegarde »*.

## Les idées hors projet
Pour les idées qui n'ont pas encore de projet : un dossier `~/Idees/` avec un fichier par idée. Le jour où une idée devient un projet, on crée son dossier avec la structure ci-dessus.

## Les bonnes pratiques valables partout
Ce qui vaut pour **tous** tes projets (ta façon de travailler, tes règles) va dans le `CLAUDE.md` **global** : `~/.claude/CLAUDE.md` (déjà installé par le kit). Le `CLAUDE.md` d'un projet ne contient que ce qui est propre à ce projet.
