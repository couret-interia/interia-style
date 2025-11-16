# InterIA Reference Repository — Structure

This document describes the recommended structure of a **reference repository**,
as used in the `INTERIA_repo` template.

The goal is to provide a clean, reproducible layout that can be cloned and adapted
for any InterIA project (proof frameworks, labs, datasets, visualizations, etc.).

---

## 1. Top-level layout

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

### 1.1 README files

- `README.md` — main entry point (EN).
- `README_FR.md` — main entry point (FR).
- `README_hero.md` — “cover / landing” page (EN) with a more polished look.
- `README_hero_FR.md` — same idea (FR).

All of them should follow the InterIA **corporate header** conventions described
in `STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` (badges, language switch, hero links).

### 1.2 STYLE_GUIDE and meta files

- `STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` — pointers to the canonical style guides in the
  `interia-style` repository. These files are not meant to be edited per-project
  beyond pointing to the central references.
- `CONTRIBUTING.md` — how to contribute to this particular repo.
- `CODE_OF_CONDUCT.md` — minimal behavioral guidelines.
- `LICENSE` — project license (e.g. MIT, Apache-2.0, GPL-3.0).

---

## 2. Source code and documentation

### 2.1 `src/`

Python (or other language) code that is **reusable** and not just a one-off experiment.

Typical layout:

```text
src/
 ├── __init__.py
 ├── module_a.py
 └── subpackage/
      └── __init__.py
```

It is recommended to avoid putting notebooks in `src/` and to keep this folder as clean
library-like code.

### 2.2 `docs/`

Long-form documentation, notes, or rendered artifacts (Markdown, HTML, etc.).

Examples:

- `docs/architecture.md` — explanation of the global architecture.
- `docs/background.md` — theoretical context.
- `docs/changelog.md` — long-form changelog if needed.

### 2.3 `figures/`

Static images (PNG, SVG, PDF…) to be referenced by READMEs, docs, LaTeX, or the Proof/Results Gallery.

---

## 3. LaTeX and articles

### 3.1 `latex/`

Holds LaTeX source files and custom classes.

Example:

```text
latex/
 ├── interia-article.cls
 └── main.tex
```

- `interia-article.cls` — optional InterIA article class (libertinus + microtype, clean typography).
- `main.tex` — main article or report.

---

## 4. GitHub Pages and Gallery

### 4.1 `pages/`

Content for GitHub Pages. The InterIA convention is to use this as a **Proof/Results Gallery** hub.

Example:

```text
pages/
 └── index.html
```

The URL is then something like:

```text
https://couret-interia.github.io/<repo>/
```

and may include a `#gallery` anchor for the Proof/Results Gallery section.

---

## 5. GitHub configuration

### 5.1 `.github/workflows/`

Continuous Integration and Pages deployment.

Typical files:

- `markdown.yml` — Markdown linting.
- `latex.yml` — optional LaTeX build.
- `pages.yml` — GitHub Pages deployment.

### 5.2 `.github/ISSUE_TEMPLATE/`

Issue templates (bug reports, feature requests, etc.).

- `bug_report.yml`
- `feature_request.yml`

### 5.3 `.github/pull_request_template.md`

Template for pull requests with checkboxes for:

- following STYLE_GUIDE,
- updating docs/READMEs,
- ensuring CI passes.

---

## 6. Using this structure for a new InterIA repository

1. Copy or clone the reference structure.
2. Rename `<repo>` everywhere to the real repository name.
3. Fill in project-specific content (code, notebooks, docs, LaTeX, figures).
4. Configure CI and GitHub Pages if needed.
5. Keep READMEs (EN/FR) and Hero pages in sync, and follow `STYLE_GUIDE` conventions.
