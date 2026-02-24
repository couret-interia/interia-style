# InterIA Math Lab — Structure du Référentiel (FR)

Ce document décrit la structure recommandée pour un **référentiel de laboratoire de mathématiques InterIA**,
tel que `interia-math-lab`.

`interia-math-lab` est destiné à héberger des **expériences numériques et analytiques exploratoires** :

- zéros de zêta, estimations de Δ₃, λ, motifs mod-30,
- spectres synthétiques, substituts de matrices aléatoires,
- notebooks Jupyter, travaux préparatoires,
- visualisations et rapports rapides.
- tout en étant reproductible (données, scripts, rapports),
- et aligné avec le style d'entreprise InterIA (README, en-têtes, galerie).

---

## 1. Mise en page de haut niveau

```text
interia-math-lab/
 ├── README.md
 ├── README_FR.md
 ├── README_hero.md
 ├── README_hero_FR.md
 ├── STYLE_GUIDE.md
 ├── STYLE_GUIDE_FR.md
 ├── CONTRIBUTING.md
 ├── CODE_OF_CONDUCT.md
 ├── LICENSE
 ├── src/
 │    ├── datasets/
 │    └── experiments/
 ├── notebooks/
 ├── data/
 │    ├── raw/
 │    └── processed/
 ├── figures/
 ├── reports/
 ├── latex/
 ├── pages/
 └── .github/
      ├── workflows/
      ├── ISSUE_TEMPLATE/
      └── pull_request_template.md
```

---

## 2. README et style

- `README.md` — page d'accueil principale (EN).
- `README_FR.md` — page d'accueil principale (FR).
- `README_hero.md` / `README_hero_FR.md` — courtes pages Hero soignées.

Les quatre devraient utiliser :

- l'en-tête InterIA (💬 Discussion, ⭐ étoiles, ✨ lien vers Hero, commutateur FR/EN),
- et suivre la structure du `STYLE_GUIDE.md`.

`STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` devrait pointer vers les fichiers de style canoniques
dans le dépôt `interia-style`.

---

## 3. Notebooks et expériences

### 3.1 `notebooks/`

C'est le **cœur du laboratoire**. Exemples :

- `01_delta3_first_experiments.ipynb`
- `02_lambda_estimation_primes.ipynb`
- `10_zeta_zeros_local_stat.ipynb`
- `99_scratchpad.ipynb`

Conventions:

- Utilisez des préfixes numérotés (`01_`, `02_`, …) pour les principales expériences.
- Réservez `9x_` ou `99_` pour les notebooks de brouillon / espace de jeux.
- Documentez les sources de données, les paramètres et les résultats dans chaque notebook.

---

## 4. Code source

### 4.1 `src/`

Aides et modules réutilisables utilisés par les carnets de notes (notebooks) ou les scripts externes.

Exemple:

```text
src/
 ├── __init__.py
 ├── datasets/
 │    ├── __init__.py
 │    └── primes.py
 └── experiments/
      ├── __init__.py
      └── delta3_tools.py
```

Directives :

- Mettez ici un code de type “bibliothèque” (fonctions, classes, utilitaires).
- Évitez de mélanger du code ad hoc ponctuel avec des outils réutilisables.

---

## 5. Mise en page des données

### 5.1 `data/raw/`

Données brutes telles qu'obtenues à partir de calculs ou de sources externes (par ex. LMFDB, exports OEIS, CSV,
JSON, etc.). Elle doit être considérée comme immuable dans la mesure du possible.

### 5.2 `data/processed/`

Données dérivées, nettoyées ou enrichies :

- courbes Δ₃ précalculées,
- estimations λ sur différentes plages,
- listes de nombres premiers filtrées, etc.

Chaque ensemble de données traité doit avoir une référence dans un notebook ou un rapport expliquant comment il
a été produit.

---

## 6. Figures et rapports

### 6.1 `figures/`

Images statiques produites par des notebooks ou LaTeX :

- graphiques (plots) de Δ₃(L),
- histogrammes des espacements,
- courbes d'estimation de λ,
- diagrammes schématiques.

### 6.2 `reports/`

Courtes résumés Markdown des résultats :

- `draft_notes.md` — notes en cours, TODOs, brouillons.
- `results_summary.md` — aperçu plus stable et de haut niveau des découvertes.

Ces rapports peuvent être liés à la Galerie de Preuves/Résultats (Proof/Results).

---

## 7. Notes LaTeX

### 7.1 `latex/`

Pour des écrits plus structurés :

```text
latex/
 ├── interia-article.cls
 └── math-lab-notes.tex
```

- `interia-article.cls` — classe d'article InterIA (facultatif).
- `math-lab-notes.tex` — notes principales agrégeant des connaissances stables du laboratoire.

---

## 8. Pages GitHub — Galerie des Résultats

### 8.1 `pages/index.html`

Page d'accueil minimale pour la **Galerie des Résultats** du laboratoire :

- liens vers des notebooks clés (ou leurs versions rendues),
- liens vers `reports/results_summary.md`,
- figures/thumbnails optionnels.

Modèle d'URL :

```text
https://couret-interia.github.io/interia-math-lab/#gallery
```

Vous pouvez ajouter des ancres (`#gallery`, `#lambda`, `#delta3`) et les styliser comme vous le souhaitez.

---

## 9. CI et modèles

### 9.1 `.github/workflows/`

- `markdown.yml` — validation Markdown.
- `pages.yml` — déploiement des Pages GitHub.

Extras optionnels :

- vérifications de l'exécution des notebooks,
- tests pour `src/`.

### 9.2 `.github/ISSUE_TEMPLATE/`

Modèles de problèmes pour :

- rapports de bogues,
- demandes de fonctionnalités.

### 9.3 `.github/pull_request_template.md`

Encouragez les contributeurs à :

- suivre le STYLE_GUIDE,
- maintenir les docs et les README à jour,
- s'assurer que l'intégration continue est réussie.

---

## 10. Utiliser cette structure pour un nouveau Lab Mathématique

1. Copier la structure de `interia-math-lab` ou de ce document.
2. Ajuster les noms (repo, chemins, préfixes de notebooks).
3. Commencer avec un seul notebook et un petit ensemble de données.
4. Promouvoir les connaissances stables dans `src/` et `reports/`.
5. Maintenir la Galerie des Résultats et les README synchronisés avec l'évolution du laboratoire.
