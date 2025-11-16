# InterIA Math Lab — Repository Structure (EN)

This document describes the recommended structure for an **InterIA math lab** repository,
such as `interia-math-lab`.

`interia-math-lab` is meant to host **exploratory numerical and analytic experiments**:

- zeta zeros, Δ₃, λ estimates, mod-30 patterns,
- synthetic spectra, random matrix surrogates,
- Jupyter notebooks, scratch work,
- visualizations and quick reports.
- yet reproducible (data, scripts, reports),
- and aligned with the InterIA corporate style (READMEs, headers, gallery).

---

## 1. Top-level layout

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

## 2. READMEs and style

- `README.md` — main landing page (EN).
- `README_FR.md` — main landing page (FR).
- `README_hero.md` / `README_hero_FR.md` — short, polished Hero pages.

All four should use:

- the InterIA header (💬 Discussion, ⭐ stars, ✨ link to Hero, FR/EN switch),
- and follow the structure from `STYLE_GUIDE.md`.

`STYLE_GUIDE.md` / `STYLE_GUIDE_FR.md` should point to the canonical style files
in the `interia-style` repository.

---

## 3. Notebooks and experiments

### 3.1 `notebooks/`

This is the **heart of the lab**. Examples:

- `01_delta3_first_experiments.ipynb`
- `02_lambda_estimation_primes.ipynb`
- `10_zeta_zeros_local_stat.ipynb`
- `99_scratchpad.ipynb`

Conventions:

- Use numbered prefixes (`01_`, `02_`, …) for main experiments.
- Reserve `9x_` or `99_` for scratch / playground notebooks.
- Document data sources, parameters, and results in each notebook.

---

## 4. Source code

### 4.1 `src/`

Reusable helpers and modules used by notebooks or external scripts.

Example:

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

Guidelines:

- Put “library-like” code here (functions, classes, utilities).
- Avoid mixing ad-hoc one-off code with reusable helpers.

---

## 5. Data layout

### 5.1 `data/raw/`

Raw data as obtained from computations or external sources (e.g. LMFDB, OEIS exports, CSV,
JSON, etc.). It should be considered immutable whenever possible.

### 5.2 `data/processed/`

Derived, cleaned, or enriched data:

- precomputed Δ₃ curves,
- λ estimates on various ranges,
- filtered prime lists, etc.

Each processed dataset should have a reference in a notebook or a report explaining how it
was produced.

---

## 6. Figures and reports

### 6.1 `figures/`

Static images produced by notebooks or LaTeX:

- plots of Δ₃(L),
- histograms of spacings,
- λ-estimation curves,
- schematic diagrams.

### 6.2 `reports/`

Short Markdown summaries of results:

- `draft_notes.md` — running notes, TODOs, scratch.
- `results_summary.md` — more stable, high-level overview of findings.

These reports can be linked from the Proof/Results Gallery.

---

## 7. LaTeX notes

### 7.1 `latex/`

For more structured write-ups:

```text
latex/
 ├── interia-article.cls
 └── math-lab-notes.tex
```

- `interia-article.cls` — InterIA article class (optional).
- `math-lab-notes.tex` — main notes aggregating stable lab insights.

---

## 8. GitHub Pages — Results Gallery

### 8.1 `pages/index.html`

Minimal landing page for the lab’s **Results Gallery**:

- links to key notebooks (or their rendered versions),
- links to `reports/results_summary.md`,
- optional figures/thumbnails.

URL pattern:

```text
https://couret-interia.github.io/interia-math-lab/#gallery
```

You can add anchors (`#gallery`, `#lambda`, `#delta3`) and style it as you like.

---

## 9. CI and templates

### 9.1 `.github/workflows/`

- `markdown.yml` — Markdown linting.
- `pages.yml` — GitHub Pages deployment.

Optional extras:

- notebook execution checks,
- tests for `src/`.

### 9.2 `.github/ISSUE_TEMPLATE/`

Issue templates for:

- bug reports,
- feature requests.

### 9.3 `.github/pull_request_template.md`

Encourage contributors to:

- follow STYLE_GUIDE,
- keep docs and READMEs up to date,
- ensure CI is green.

---

## 10. Using this structure for a new Math Lab

1. Copy the structure from `interia-math-lab` or from this document.
2. Adjust names (repo, paths, notebook prefixes).
3. Start with a single notebook and small dataset.
4. Promote stable insights into `src/` and `reports/`.
5. Keep the Results Gallery and READMEs in sync with the lab’s evolution.
