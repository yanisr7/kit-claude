# Guide — Apprendre à bosser avec Claude

## 1. L'idée
Tu ne codes pas : tu **pilotes**. Tu décris le résultat voulu, Claude propose un plan, tu valides, il fait, tu vérifies. Ton job : avoir les idées, donner le contexte, juger le résultat.

## 2. Ouvrir Claude
- Dans un terminal : va dans le dossier du projet (`cd ~/Projets/mon-site`) puis tape `claude`.
- Ou dans **Cursor / VS Code** avec l'extension Claude Code (le plus confortable).
- Une conversation = un sujet. Nouveau sujet → `/clear`.

## 3. Bien parler à Claude
| ❌ Flou | ✅ Clair |
|---|---|
| « fais un site » | « fais une page de présentation pour ma marque de t-shirts, 3 sections : héros avec photo, les produits, contact. Style sobre noir et blanc. Propose le plan d'abord. » |
| « c'est moche » | « le titre est trop gros sur mobile et les boutons sont collés, mets de l'espace » + capture d'écran |
| « ça marche pas » | « quand je clique sur Acheter, rien ne se passe. Voilà le message d'erreur : … » |

Astuces :
- **Glisse des captures d'écran** dans la conversation : Claude les voit.
- Demande **« pourquoi ? »** dès que tu ne comprends pas un choix. C'est comme ça qu'on apprend.
- Si Claude part dans la mauvaise direction : **Échap** pour l'arrêter, et recadre.
- **« Propose le plan d'abord »** = la phrase magique pour les grosses tâches.

## 4. Les commandes utiles
- `/clear` — repartir à zéro
- `/plugin` — voir/installer des skills
- `/mcp` — voir les outils connectés (Obsidian, X, Apify) et se connecter
- `/model` — changer de modèle
- « **sauvegarde** » — Claude met à jour le Journal du projet dans Obsidian
- « **retiens que…** » — Claude garde une préférence en mémoire

## 5. Les skills (ce que Claude sait faire en plus)
Il les utilise tout seul, mais tu peux les nommer :
- **superpowers** : brainstorming, plans, débogage méthodique, vérification avant de dire « fini ».
- **document-skills** : PowerPoint, Word, Excel, PDF.
- **example-skills** : tester un site web (Playwright), design de pages, etc.
- **marketing-skills** : copywriting, SEO, emails, contenu réseaux.

## 6. Nos workflows (les recettes)
Dans `~/kit-claude/recettes/` :
- `montage-video.md` — rushs → montage auto → Premiere
- `recherche-x.md` — veille Twitter
- `shopify.md` — modifier une boutique sans casser le live
- `presentations.md` — decks, pages de présentation, factures
- `obsidian.md` — le cerveau / la mémoire des projets

## 7. Les règles d'or
1. **Plan → validation → action.** Jamais l'inverse sur un truc important.
2. **Git = bouton annuler.** Commit + push après chaque étape réussie.
3. **Rien en live sans le vérifier** (site, boutique, post).
4. **Jamais de clé API ou mot de passe** sur GitHub ou dans un message public.
5. **Ne jamais laisser Claude inventer** des chiffres, des infos légales ou des citations. Il doit demander.
6. **Toujours vérifier toi-même** le résultat (ouvrir la page, regarder la vidéo).

## 8. Exercices pour démarrer (dans l'ordre)
1. **Cerveau** : *« Crée un dossier projet "Mon portfolio" dans mon cerveau Obsidian et explique-moi chaque fichier. »*
2. **Recherche X** : *« Cherche sur Twitter ce que les gens font avec Claude Code pour le montage vidéo. Résume en 5 points + ce que je pourrais tester. »*
3. **Page web** : *« Crée-moi une page portfolio simple en HTML avec mes passions, propose le plan d'abord. »* Puis : *« mets-la sur GitHub »*, puis *« déploie-la sur Vercel »*.
4. **Vidéo** : filme 3-4 rushs de toi qui parles (téléphone), puis suis `recettes/montage-video.md` pour en faire un reel de 45 s.
5. **Deck** : *« Fais-moi un PowerPoint de 6 slides qui présente mon projet de portfolio. »*
6. **Sauvegarde** : à la fin, dis *« sauvegarde »* et va lire ton `Journal.md` dans Obsidian.

Bloqué ? Demande à Claude : *« lis ~/kit-claude/GUIDE.md et aide-moi sur l'étape X »*.
