# 🏛️ InterIA Corporate Suite

## 1. 📘 Templates README (Standard + Hero)

### 1.1. README.md (EN)

```md
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

Short description (1–2 lines).

---

## 🪶 About this project
Explain scope, goals, context.

## 🔧 Reproducibility
Explain folders, structure, CI, build commands.

## 📚 Proof Gallery
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

## 🔖 Citation
(BibTeX block)

---
```

---

### 1.2. README_FR.md (FR)

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

# 🧠 <Nom du Projet> — InterIA

Description courte (1–2 lignes).

---

## 🪶 À propos
Objectifs, contexte, public.

## 🔧 Reproductibilité
Structure, build, CI.

## 📚 Proof Gallery
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

## 🔖 Référence
(BibTeX)

---
```

---

### 1.3. README_hero.md (EN)

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

# 🧠 InterIA — <Tagline>

> **Status:** proof-only · reproducible · non-resolutive (RH remains open)

### 🪶 About
Short description.

### 📚 Proof Gallery
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)

### 🔖 Citation
Link to README.
```

---

### 1.4. README_hero_FR.md (FR)

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

> **Statut :** preuve-seule · reproductible · non-résolutif

### 🪶 À propos
Brève description.

### 📚 Proof Gallery
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)
```

---

## 2. 🤝 CONTRIBUTING.md (EN/FR)

### CONTRIBUTING.md

```md
# Contributing to InterIA

Thank you for considering contributing!

## Code Style
- Python: PEP8 + type hints
- Markdown: [Use the InterIA STYLE_GUIDE](https://github.com/couret-interia/STYLE_GUIDE.md)
- LaTeX: libertinus, clean sectioning, no colors

## How to Contribute
1. Fork the repo
2. Create a branch: `git checkout -b feature/<name>`
3. Submit a Pull Request

## Issues
Use issue templates in `.github/ISSUE_TEMPLATE/`.

## Communication
Main channel: GitHub Discussions
```

### 2.2 CONTRIBUTING_FR.md

```md
# Contribuer à InterIA

Merci de considérer votre contribution !

## Style de Code
- Python : PEP8 + annotations de type
- Markdown : [Voir le "Guide de style" InterIA](https://github.com/couret-interia/STYLE_GUIDE_FR.md)
- LaTeX : libertinus, sectionnement propre, pas de couleurs

## Comment Contribuer
1. Forkez le repo
2. Créez une branche : `git checkout -b feature/<nom>`
3. Soumettez une Pull Request

## Problèmes
Utilisez les modèles de problème dans `.github/ISSUE_TEMPLATE/`.

## Communication
Canal principal : Discussions GitHub
```

---

## 3. 📜 CODE_OF_CONDUCT.md

```md
# InterIA Code of Conduct / Code de Conduite

[We follow](https://github.com/couret-interia/CODE_OF_CONDUCT.md) the / [Nous suivons](https://github.com/couret-interia/CODE_OF_CONDUCT_FR.md) le Contributor Covenant v2.1.

Be respectful · Be clear · Assume good intent · No harassment · No exclusion.
```

---

## 4. ⚙️ GitHub Issue Templates

Dans `.github/ISSUE_TEMPLATE/` :

### 4.1 Bug report

```yml
name: Bug Report
description: Report a problem
body:
- type: textarea
  id: what
  attributes:
    label: Problem
    placeholder: Describe clearly
  validations:
    required: true
```

### 4.2 Feature request

### 4.3 Documentation issue

Je te fournis les fichiers complets si tu veux.

---

## 5. 🔄 Pull Request Template

`.github/pull_request_template.md`

```md
# Pull Request

## Summary
(What does this PR do?)

## Checklist
- [ ] Follows STYLE_GUIDE.md
- [ ] Documentation updated
- [ ] CI passing
```

---

## 6. 🧪 CI Corporate

### 6.1 Markdown Linter

`.github/workflows/markdown.yml`

```yml
name: Markdown Lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DavidAnson/markdownlint-cli2-action@v16
```

---

## 7. 📘 Template LaTeX InterIA

`interia-article.cls`

```tex
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{interia-article}[2025/01/01 InterIA Article Class]

\LoadClass{article}
\usepackage{libertinus}
\usepackage{microtype}

\setlength{\parskip}{6pt}
\setlength{\parindent}{0pt}
```

---

## 8. 🌐 GitHub Pages Template (Proof Gallery)

`index.html` minimal :

```html
<html>
<head>
  <title>InterIA Proof Gallery</title>
</head>
<body>
  <h1>Proof Gallery</h1>
  <ul>
    <li><a href="docs/proof.pdf">Proof</a></li>
    <li><a href="figures/diagram.png">Diagram</a></li>
  </ul>
</body>
</html>
```

---

## 9. 🏗️ Structure d’un dépôt InterIA

```
<repo>/
 ├── README.md
 ├── README_FR.md
 ├── README_hero.md
 ├── README_hero_FR.md
 ├── STYLE_GUIDE.md (link or copy)
 ├── CONTRIBUTING.md
 ├── CODE_OF_CONDUCT.md
 ├── docs/
 ├── figures/
 ├── src/
 ├── .github/
 │    ├── workflows/
 │    └── ISSUE_TEMPLATE/
```

---

## 🔟 Script Python de création automatique

`interia_init.py`

```python
import os, shutil

FILES = ["README.md","README_FR.md","README_hero.md","README_hero_FR.md",
         "CONTRIBUTING.md","CODE_OF_CONDUCT.md"]

def init(repo):
    os.makedirs(repo, exist_ok=True)
    for f in FILES:
        with open(os.path.join(repo, f), "w") as out:
            out.write(f"# {f} — To Fill\n\n")
    print("InterIA repository initialized.")

if __name__ == "__main__":
    init("new_interia_repo")
```

---