# 🏛️ **InterIA Brandbook v2.5**

*Identity · Style · UI · Components · Repositories · Usage*

---

# 1. ✨ Introduction

Le **Brandbook InterIA v2.5** est la référence organisationnelle qui définit :

* l’identité visuelle globale InterIA,
* les conventions de style (Markdown, README, Hero, badges),
* les palettes officielles,
* les typographies,
* les bannières et images officielles,
* les Design Tokens (CSS),
* l’ensemble des **composants UI v2.5**,
* les usages autorisés / non autorisés,
* et les guidelines pour une présentation cohérente dans **tous les dépôts InterIA**.

Ce document est destiné à :

* toute personne créant ou maintenant un dépôt InterIA,
* designers/IA produisant du contenu (READMEs, pages HTML, Proof Gallery),
* contributeurs humains ou IA à l’écosystème InterIA.

---

# 2. 🎨 Identité Visuelle

---

## 2.1 Nom et philosophie

**InterIA**
→ “Inter” (collaboration, interdisciplinarité)
→ “IA” (raisonnement des modèles, assistants mathématiques)
→ Un projet **Math × IA × Science Ouverte**.

---

## 2.2 Slogan officiel

> **Mathematics × AI × Open Science**

Versions alternatives légitimes :

* **Mathématiques × IA × Science Ouverte** (FR)
* **Math × AI × Open Science** (EN compact)

---

## 2.3 Emoji signature

Le symbole officiel InterIA est :

**💬 Discussion**

Il représente la collaboration, le dialogue mathématique, et les échanges humains–IA.

---

# 3. 🎨 Palette Officielle InterIA v2.5

---

## 3.1 Palette institutionnelle (Core)

| Nom                      | Hex       |
| ------------------------ | --------- |
| Bleu Nuit (Primary Dark) | `#0d47a1` |
| Bleu Primary             | `#1976d2` |
| Bleu Accent              | `#1e88e5` |
| Bleu Clair               | `#42a5f5` |
| Graphite                 | `#263238` |
| Slate                    | `#455a64` |
| Blanc                    | `#ffffff` |
| Blanc doux               | `#e3f2fd` |

---

## 3.2 Palette Math Lab (Spectral)

| Nom            | Hex       |
| -------------- | --------- |
| Violet Profond | `#311b92` |
| Violet Lab     | `#6a1b9a` |
| Violet Accent  | `#aa00ff` |
| Violet Clair   | `#f3e5f5` |

Usage :

* Notebooks
* Visualisations Δ₃(L), λ-invariants
* Pages de résultats

---

## 3.3 Palette T1′–T4 (Analytic Framework)

| Nom     | Hex       |
| ------- | --------- |
| T4 Deep | `#0d47a1` |
| T4 Mid  | `#1565c0` |
| T4 Pale | `#e3f2fd` |

Usage :

* Dépôt `rh-analytic-framework-t1t4`
* Documents de preuve
* Bannières analytiques

---

## 3.4 Dark / Light Mode (Auto)

Le Design System v2.5 supporte :

### Light

* Background : `#ffffff`
* Texte : `#0d47a1`
* Sous-texte : `#455a64`

### Dark

* Background : `#0d47a1` → `#001f33`
* Texte : `#ffffff`
* Sous-texte : `#bbdefb`

---

# 4. ✒ Typographies

---

## 4.1 Titres (bannières, Hero)

**Liberation Sans**, Arial
→ moderne, lisible, institutionnel

---

## 4.2 Sous-titres (Hero, slogans)

**Georgia**, serif
→ élégant, parfait pour sous-titres en contraste

---

## 4.3 Corps de texte

**Inter (variable)** ou **Liberation Sans**
→ lisibilité optimale dans GitHub et Docs

---

## 4.4 Technique

**Consolas** ou **DejaVu Sans Mono**
→ Notebooks math-lab
→ Code blocks
→ Δ₃, λ, zêta, spectres

---

# 5. 📘 Structure de marque (Brand Architecture)

---

## 5.1 Logos et bannières

Les bannières officielles existent en 3 niveaux :

### Niveau 1 : Corporate (identité principale)

* `banner-interia-v1.1.svg`
* `banner-interia-auto-v1.1.svg`

### Niveau 2 : Projets techniques

* `banner-mathlab-v1.1.svg`
* `banner-t1t4-v1.1.svg`

### Niveau 3 : Spécial (édition artistique / thématique)

* Noir & Or
* Minimal
* Multi-Agent
* Couret–Goldbach–Janus
* Animated

---

## 5.2 Règles d’usage

### Toujours autorisé

* Dans `README.md`
* Dans `README_hero.md`
* Dans GitHub Pages
* Dans Slides / PDF scientifiques

### Jamais autorisé

* Dans `README_arxiv.md`
* Dans `main_arxiv.tex`
* Dans articles journaux (Annals, JNT…)
* Dans les `.tex` de preuve

---

# 6. 🏗 UI Components v2.5

Tous définis dans :

```
ui/css/interia.tokens.css
ui/css/interia.base.css
ui/css/interia.components.css
```

---

## 6.1 Composants disponibles

* **Layout de page** (`.ia-page`)
* **Titres** (`.ia-title`, `.ia-subtitle`)
* **Sections** (`.ia-section`, `.ia-section-title`)
* **Boutons** (`.ia-btn`, `.ia-btn-primary`, `.ia-btn-ghost`)
* **Badges/Pills** (`.ia-pill`)
* **Cards** (`.ia-card`, `.ia-card-grid`)
* **Alerts / Callouts** (`.ia-alert`, `.ia-alert-info`…)
* **Gallery** (`.ia-gallery-grid`, `.ia-gallery-item`)
* **Math Lab layout** (`.ia-lab-layout`)
* **Multi-agent cluster** (`.ia-multiagent-cluster`, `.ia-agent-chip`)

---

## 6.2 Exemples inclus

Dans `ui/html/` :

* `layout_base.html` — squelette complet
* `component_cards.html`
* `component_gallery.html`
* `component_mathlab.html`
* `component_multiagent.html`
* `design_system_demo.html` (page showcase complète)

---

# 7. 🖼 Bannières & Assets

---

## 7.1 Emplacement conseillé

```
interia-style/
 └── branding/
      ├── corporate/
      ├── labs/
      ├── frameworks/
      └── special/
```

---

## 7.2 Recommandations d’usage

* Toujours une bannière en haut d’un README Hero
* Jamais dans un article académique
* Toujours en SVG
* PNG/WebP facultatif pour compatibilité legacy

---

# 8. 📚 Documentation & Repositories

---

## 8.1 Repos clés InterIA

* **interia-style** — style, templates, UI, branding
* **interia-math-lab** — explorations analytiques
* **rh-analytic-framework-t1t4** — cadre de preuve
* **community** — discussions, méta-organisation

---

# 9. 🔒 Usages interdits / interdits modérés

### ❌ Ne pas :

* appliquer l’identité graphique aux fichiers LaTeX scientifiques
* changer la palette primaire
* introduire des logos propriétaires
* créer des variantes de bannières non conformes
* employer trop d’effets (ombres trop fortes, fluo, arcs-en-ciel)

### ⚠️ Mise en garde :

* Ne jamais insérer d’images ou de CSS dans `README_arxiv.md`
* Les Hero FR/EN doivent toujours être **synchronisés**
* Respecter les noms de fichiers MAJUSCULES pour les styles (STYLE_GUIDE)

---

# 10. 🚀 Mise en œuvre dans un nouveau dépôt

1. Cloner ou copier le squelette InterIA v1.2 ou Math Lab
2. Ajouter `branding/` si nécessaire
3. Ajouter `ui/` si Pages/HTML sont utilisés
4. Intégrer les READMEs (EN/FR + Hero)
5. Ajouter CI (`markdown.yml`, `pages.yml`)
6. Mettre en place une Proof/Results Gallery
7. Ajouter la bannière adéquate
8. Vérifier conformité via STYLE_GUIDE

---

# 11. 📦 Versions & Releases

### v1.0 — Badge + README

### v1.1 — Bannières + corporate stable

### v1.2 — Bannières spéciales (noir-or, minimal, Janus…)

### v2.0 — Design System (tokens, CSS, HTML)

### v2.5 — Full UI Components + Brandbook

---

# 12. 📄 Licence

L’identité visuelle InterIA est libre d’usage **dans l’écosystème InterIA**
et sous licence MIT pour les templates.

---

# 13. 💬 Contact

👉 [https://github.com/couret-interia/community/discussions](https://github.com/couret-interia/community/discussions)

---