# 🏛️ InterIA Corporate Style Guide

**Version : 1.0.0**
**Scope :** READMEs, Hero pages, GitHub Pages, dépôt LaTeX (meta / presentation layer)

---

## 🌐 1. Goals of the InterIA Corporate Style

This file defines the **official corporate style** for the InterIA organization.

It covers:

- headers (badges, language switches)
- README templates (EN & FR)
- Hero README templates (EN & FR)
- links to the Proof Gallery
- general rules about where *not* to use the corporate layer

---

The style aims to provide:

- **Cohesion** across all repositories under `couret-interia`
- **Scientific professionalism** (journal-ready & arXiv-compatible)
- **Lightweight visual identity** (no intrusive logos)
- **Bilingual accessibility** (FR/EN)
- **Low maintenance overhead** (one badge, one pattern)

This style applies to:

- `README.md`
- `README_FR.md`
- `README_hero.md`
- `README_hero_FR.md`
- all future variations (replication, new projects)

It **does not** apply to:

- `README_arxiv.md`
- any LaTeX source (e.g. `main_arxiv.tex`, `src/main_journal*.tex`)
- appendices and theorem files

---

## 🎨 2. Official Header (Badges + Navigation)

The official header appears at the top of:

- `README.md`
- `README_FR.md`
- `README_hero.md`
- `README_hero_FR.md`

### 📌 General header rules

It is always right-aligned and always follows this **order**:

1. 💬 Discussion badge (link to GitHub Discussions)
2. GitHub stars badge (for the current repo)
3. ✨ link to the Hero page of the same language
4. Language switch (FR ↔ EN)

- **Never** in `README_arxiv.md`.
- **No space** in `<a>` tag for badge `<img>` (prevent underline).
- **Always at the top** of the file.

### 🔷 2.1 Header for main README (EN)

Use this for `README.md` in an InterIA repo:

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions">    <img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero.md"><sup>✨</sup></a>
  <sup> · </sup>
  <a href="README_FR.md"><sup>🇫🇷</sup></a>
</p>
```

### 🔶 2.2 Header for main README_FR (FR)

Use this for `README_FR.md`:

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero_FR.md"><sup>✨</sup></a>
  <sup> · </sup>
  <a href="README.md"><sup>🇬🇧</sup></a>
</p>
```

### 2.3 🔷 Header for Hero README (EN)

Use this for `README_hero.md`:

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero_FR.md"><sup>✨🇫🇷</sup></a>
  <sup> · </sup>
  <a href="README.md"><sup>🇬🇧</sup></a>
</p>
```

### 🔶 2.4 Header for Hero README (FR)

Use this for `README_hero_FR.md`:

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero.md"><sup>✨🇬🇧</sup></a>
  <sup> · </sup>
  <a href="README_FR.md"><sup>🇫🇷</sup></a>
</p>
```

The idea is:

- each README points to the **Hero of its own language** via ✨
- the last link is always the **language switch** (FR ↔ EN)

---

## 3. 🖥️ Typography & Layout Guidelines

### Big titles

- Use `#` then `##`, rarely `###` (avoid `####` and deeper).

### Body

- Use short paragraphs and clear bullet lists.

### Important elements

- Use blockquotes `> …` for disclaimers, status, or important warnings.
- Use `---` (horizontal rule) to separate major sections.
- Avoid excessive bold/italic styling.

### ⚠️ **Code Blocks** (```` ``` ````) Inside a `Code Block`

> Generally, the *text/code* is **encapsulated** by the famous three backticks (`` ` ``); \
> Having one or more code blocks is enough to break the HTML display.

- 💠 To avoid this, **encapsulate** with more \` than the **code blocks inside**. \
• See the two chapters of the Template README in `source` mode (there are 4 \` used to prevent breaking at the end of the block ```` ```bibtex ````).
- 💡 Look for **markdown** in your *browser extensions* (or use an **md viewer** online).

<details><summary>

### 🛡️ InterIA Anti-Break Markdown Rule

</summary>

When a code block (```` ``` `````) must contain another code block:

1. Always use an external code *fence* with a **higher number of backticks**:
   - ````` ````md ````` for the outer block
   - ```` ```bash ```` for the inner block
2. Always close the fences using **the exact same sequence** used at opening.
3. If the content risks breaking the rendering, use:
   - the alternative `~~~` fences,
   - or indentation with `    ` (4 spaces).

To guarantee perfectly stable Markdown rendering (GitHub / GitLab / Pandoc / ChatGPT / IDE),
any *code block containing another code block* must use one of the 3 methods below.

---

### ✔️ 1) Classic method — Longer outer fence

````md
```bash
python script.py
```
````

- The outer block uses five backticks (`````).
- The inner block uses three (```).
- No collision is possible.

⚠️ Some lightweight editors may mis-highlight it,
but **the final HTML rendering will be correct**.

---

### ✔️ 2) Alternative method — `~~~` fences (tildes)

<!-- markdownlint-disable code-fence-style -->
~~~md
```bash
python script.py
```
~~~
<!-- markdownlint-enable code-fence-style -->

- *Tildes* are recognized by all modern Markdown engines.
- They allow embedding triple backticks without conflict.
- ✔ Safe **as long as the internal code does not contain `~~~`**.

⚠️ If the internal code **also** contains `~~~`, this method may fail.

---

### ✔️ 3) Alternative method — Indentation (4 spaces)

```md
    ```bash
    python script.py
    ```
```

- Requires **at least 4 spaces** of indentation.
- Works reliably on *all* platforms.
- Less elegant, but **fool-proof** for complex content.

---

### 🎯 Important note

Some sequences such as:

- \` \`\`\` \`
- or (```` ``` ````)

must never appear **directly** in raw text, as they may be interpreted as the start/end of a fence.

Always use one of the following escapes:

- between outer fences:
  (```` ``` ````)

- or in escaped form (maximum safety):
  (\\\`\\\`\\\`)

These rules guarantee stable rendering in *every* environment
(GitHub, GitLab, ChatGPT, Pandoc, Obsidian, VSCode…).

</details>

---

## 🧩 4. Canonical Structure for README.md

This is a recommended skeleton for `README.md` in InterIA repositories.

### 📄 4.1 Template README.md (EN)

````md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero.md"><sup>✨</sup></a>
  <sup> · </sup>
  <a href="README_FR.md"><sup>🇫🇷</sup></a>
</p>

# 🧠 <Project Name> — InterIA

Short project description (1–2 lines).

---

## 🪶 About this release

Explain the goal of the project, high-level context, and audience.

## 🔧 Reproducibility & CI

Describe:

- the code / LaTeX layout (folders, main files),
- how to build the artifacts (PDF, HTML, data),
- how CI is configured (e.g. `latex.yml`, `tests.yml`).

## 📚 Proof Gallery

Point to the GitHub Pages gallery:

[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

This page is the canonical home for:

- proof journals
- λ audits
- dependency maps
- large-format figures

## 🔖 Citation

Provide a BibTeX entry (FR & EN variants if needed).

```bibtex
@misc{interia_example_2025,
  author  = {{InterIA Collective}},
  title   = {<Title of the Work>},
  year    = {2025},
  howpublished = {\url{https://github.com/couret-interia/<repo>}},
  url          = {https://github.com/couret-interia/<repo>},
  note    = {Short description of the contribution.}
}
```

---
````

---

### 📄 4.2 Template README_FR.md (FR)

````md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero_FR.md"><sup>✨</sup></a>
  <sup> · </sup>
  <a href="README.md"><sup>🇬🇧</sup></a>
</p>

# 🧠 <Nom du Projet> — InterIA

Description courte (1–2 lignes).

---

## 🪶 À propos de cette publication

Présenter :

- le contexte,
- les objectifs,
- le type de public visé (recherche, enseignement, open science).

## 🔧 Reproductibilité & CI

Décrire :

- la structure du dépôt (code, LaTeX, données),
- comment construire les artefacts (PDF, HTML, notebooks),
- les workflows CI utilisés.

## 📚 Proof Gallery

Lien vers la page GitHub Pages principale :

[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

Cette page est la source canonique pour :

- les journaux de preuve,
- les audits λ,
- les schémas grand format,
- les visualisations interactives.

## 🔖 Référence

Bloc BibTeX :

```bibtex
@misc{interia_exemple_2025,
  author  = {{Collectif InterIA}},
  title   = {<Titre du travail>},
  year    = {2025},
  howpublished = {\url{https://github.com/couret-interia/<repo>}},
  url          = {https://github.com/couret-interia/<repo>},
  note    = {Brève description de la contribution.}
}
```

---
````

---

## 🌅 5. Canonical Structure for README Hero

Hero READMEs are short, “cover-style” entry points with a more polished look, meant to be used as landing pages (and linked from badges, GitHub Pages, etc.).

### 📄 5.1 Hero README (EN) — `README_hero.md`

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero_FR.md"><sup>✨🇫🇷</sup></a>
  <sup> · </sup>
  <a href="README.md"><sup>🇬🇧</sup></a>
</p>

# 🧠 InterIA — <Hero Tagline>

One–two lines of high-level description.

---

> 🧮 **Status:** proof-only · reproducible · non-resolutive (RH remains open).

> 🧾 **Maintained by:** <names> & the **InterIA Collective**

---

### 🪶 About this hero

Short explanation of what this hero page is (landing, public entry, etc.).

### 📚 Explore the Proof Gallery

[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

---

### 🔖 Citation

(Optionally repeat the BibTeX here, or link to the main README.)
```

---

### 📄 5.2 Hero README (FR) — `README_hero_FR.md`

```md
<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/<repo>/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/<repo>.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero.md"><sup>✨🇬🇧</sup></a>
  <sup> · </sup>
  <a href="README_FR.md"><sup>🇫🇷</sup></a>
</p>

# 🧠 InterIA — <Slogan Hero>

Une à deux phrases de description.

---

> 🧮 **Statut :** preuve-seule · reproductible · non-résolutif (RH demeure ouverte).

> 🧾 **Entretien :** <noms> et le **Collectif InterIA**

---

### 🪶 À propos de ce hero

Courte explication du rôle de cette page (landing, porte d’entrée publique, etc.).

### 📚 Explorer la Proof Gallery

[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

---

### 🔖 Référence

(Éventuellement répéter le BibTeX ou renvoyer vers le README principal.)
```

---

## 📁 6. Files that MUST Stay “Plain”

Do **not** apply the corporate header or styling to:

- `README_arxiv.md`
- `main_arxiv.tex`
- `main_journal*.tex`
- `appendix/*.tex`
- `theorems/*.tex`
- journal submission versions (e.g. for Annals, JNT, etc.)

These should remain as neutral and minimal as possible to match academic standards.

---

## 🔧 7. Color Palette & Identity

### Guiding colors

| Element          | Color          | Usage                                 |
| ---------------  | ---------------| ------------------------------------- |
| Light blue       | `#1e88e5`      | Discussion badge                      |
| Midnight blue    | `#0d47a1`      | Label background                      |
| Black/Anthracite | GitHub default | Titles, text                          |
| `*`Emoji 💬      | invariant      | InterIA identity (open communication) |

`*` Is the canonical symbol for InterIA “open discussion”.

- No heavy branding, no logos in PDFs unless explicitly required.

### LaTeX style (optional)

For PDF documents, use:

- `\usepackage{libertinus}`
- simple titles
- no colored logos

---

## 📐 8. Proof Gallery Link (Canonical)

In all main READMEs and heroes, use:

```md
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)
```

Where `<repo>` is the repository name (e.g. `rh-analytic-framework-t1t4`).

The Proof Gallery becomes the **canonical hub** for:

- proof journals,
- λ audits,
- dependency maps,
- large-format visual explanations.

---

## 🧪 9. Intégration CI/CD

Conventions CI :

- `latex.yml` for build PDF
- `pages.yml` for GitHub Pages
- `linter.yml` optional for Markdown

---

## 🧭 10. Versioning

This style guide version:

- **v1.0.0**

Future updates (v1.1, v1.2, …) can extend:

- dark-mode aware color hints,
- additional templates (e.g. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`),
- MkDocs or Sphinx documentation themes aligned with this style.

---
