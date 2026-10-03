# Recette — Modifier un thème Shopify avec Claude

**Règle d'or : on travaille sur un thème BROUILLON, jamais sur le thème live.** On ne publie qu'après validation.

## Mise en place (une fois par boutique)
1. `brew install shopify-cli` (ou demande à Claude).
2. Dans l'admin Shopify : Boutique en ligne → Thèmes → **Dupliquer** le thème live → c'est ton brouillon.
3. `shopify theme pull --store ta-boutique` → récupère le code en local, puis `git init` + push sur GitHub (sauvegarde).
4. Note l'ID du thème brouillon dans le `État Actuel.md` du projet.

## Boucle de travail
1. Tu décris ce que tu veux, avec une **capture d'écran** si possible : *« sur mobile, mets le titre au-dessus du texte »*.
2. Claude modifie le fichier Liquid concerné.
3. Il pousse **uniquement ce fichier** vers le brouillon :
   `shopify theme push --theme <ID_BROUILLON> --only sections/xxx.liquid --nodelete`
4. Tu vérifies sur le lien d'aperçu du brouillon (mobile + ordi).
5. Commit + push GitHub.
6. Quand tout est bon : **toi** tu publies le brouillon depuis l'admin.

## Contenu produit (fiches, descriptions, métachamps)
- Ces modifs sont **live immédiatement** → demander à Claude une **sauvegarde** (export) avant.
- Les textes répétés par produit → métachamps `custom.*` plutôt que du texte en dur dans le thème.
