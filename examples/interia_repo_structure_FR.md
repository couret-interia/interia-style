# InterIA — Référentiel de Référence — Structure

Ce document décrit la structure recommandée d'un **référentiel de référence**,
tel qu'utilisé dans le modèle `INTERIA_repo`.

L'objectif est de fournir une mise en page propre et reproductible qui peut être clonée et adaptée
pour n'importe quel projet InterIA (cadres de preuve, laboratoires, ensembles de données, visualisations, etc.).

---

## 1. Mise en page de haut niveau

```text
<repo>/
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
 ├── docs/
 ├── figures/
 ├── latex/
 ├── pages/
 └── .github/
      ├── workflows/
      └── ISSUE_TEMPLATE/
```

### 1.1 Fichiers README

- `README.md` — point d'entrée principal (EN).
- `README_FR.md` — point d'entrée principal (FR).
- `README_hero.md` — page “couv/accueil” (EN) avec un aspect plus soigné.
- `README_hero_FR.md` — même idée (FR).

Tous devraient suivre les conventions **d'en-tête corporative** InterIA décrites
dans `STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` (badges, commutateur de langue, liens hero).

### 1.2 STYLE_GUIDE et fichiers meta

- `STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` — références aux guides de style canoniques dans le
  dépôt `interia-style`. Ces fichiers ne doivent pas être modifiés par projet
  au-delà de renvoyer aux références centrales.
- `CONTRIBUTING.md` — comment contribuer à ce référentiel particulier.
- `CODE_OF_CONDUCT.md` — directives comportementales minimales.
- `LICENSE` — licence du projet (par ex. MIT, Apache-2.0, GPL-3.0).

---

## 2. Code source et documentation

### 2.1 `src/`

Code Python (ou autre langage) qui est **réutilisable** et pas seulement une expérience ponctuelle.

Mise en page typique :

```text
src/
 ├── __init__.py
 ├── module_a.py
 └── subpackage/
      └── __init__.py
```

Il est recommandé d'éviter de mettre des notebooks dans `src/` et de garder ce dossier comme un code propre
de type bibliothèque.

### 2.2 `docs/`

Documentation de longue durée, notes ou artefacts rendus (Markdown, HTML, etc.).

Exemples :

- `docs/architecture.md` — explication de l'architecture globale.
- `docs/background.md` — contexte théorique.
- `docs/changelog.md` — changelog détaillé si nécessaire.

### 2.3 `figures/`

Images statiques (PNG, SVG, PDF…) à référencer par les README, docs, LaTeX ou la Galerie de Preuves/Résultats.

---

## 3. LaTeX et articles

### 3.1 `latex/`

Contient les fichiers source LaTeX et les classes personnalisées.

Exemple :

```text
latex/
 ├── interia-article.cls
 └── main.tex
```

- `interia-article.cls` — classe d'article InterIA optionnelle (libertinus + microtype, typographie propre).
- `main.tex` — article ou rapport principal.

---

## 4. Pages GitHub et Galerie

### 4.1 `pages/`

Contenu pour les Pages GitHub. La convention InterIA est de l'utiliser comme un hub de **Galerie de Preuves/Résultats**.

Exemple :

```text
pages/
 └── index.html
```

L'URL est alors quelque chose comme :

```text
https://couret-interia.github.io/<repo>/
```

et peut inclure un ancre `#gallery` pour la section Galerie de Preuves/Résultats.

---

## 5. Configuration GitHub

### 5.1 `.github/workflows/`

Intégration Continue et déploiement des Pages.

Fichiers typiques :

- `markdown.yml` — validation Markdown.
- `latex.yml` — construction LaTeX optionnelle.
- `pages.yml` — déploiement des Pages GitHub.

### 5.2 `.github/ISSUE_TEMPLATE/`

Modèles de problèmes (rapports de bogues, demandes de fonctionnalités, etc.).

- `bug_report.yml`
- `feature_request.yml`

### 5.3 `.github/pull_request_template.md`

Modèle pour les demandes d'extraction avec cases à cocher pour :

- suivre le STYLE_GUIDE,
- mettre à jour les docs/README,
- s'assurer que l'intégration continue passe.

---

## 6. Utiliser cette structure pour un nouveau référentiel InterIA

1. Copier ou cloner la structure de référence.
2. Renommer `<repo>` partout au nom réel du référentiel.
3. Remplir le contenu spécifique au projet (code, notebooks, docs, LaTeX, figures).
4. Configurer l'intégration continue et les Pages GitHub si nécessaire.
5. Maintenir les README (EN/FR) et les pages Hero synchronisés, et suivre les conventions du `STYLE_GUIDE`.
