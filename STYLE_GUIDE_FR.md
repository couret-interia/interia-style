# 🏛️ InterIA Corporate Style Guide

**Version : 1.0.0**
**Scope :** READMEs, Hero pages, GitHub Pages, dépôt LaTeX (meta / presentation layer)

---

## 🌐 1. Objectifs du style corporatif InterIA

Ce guide définit la **charte visuelle et éditoriale officielle** de l’organisation **InterIA**.

Il couvre :

- en-têtes (badges, sélecteur de langue)
- README templates (EN & FR)
- Hero README templates (EN & FR)
- liens vers la galerie de preuves
- règles générales concernant les cas où il ne faut *pas* utiliser la couche corporative

---

Il assure :

- **Cohérence** entre tous les dépôts
- **Professionnalisme scientifique** (journal-ready & arXiv-compliant)
- **Identité visuelle légère** (sans logos intrusifs)
- **Accessibilité bilingue FR/EN**
- **Simplicité de maintenance**

Il s’applique à :

- `README.md`
- `README_FR.md`
- `README_hero.md`
- `README_hero_FR.md`
- toutes les futures variations (réplication, nouveaux projets)

Il **ne s’applique pas** à :

- `README_arxiv.md`
- toutes sources LaTeX scientifiques (ex. `main_arxiv.tex`, `src/main_journal*.tex`)
- annexes scientifiques

---

## 🎨 2. En-tête officiel (badges + navigation)

L'en-tête officiel apparaît en haut de :

- `README.md`
- `README_FR.md`
- `README_hero.md`
- `README_hero_FR.md`

### 📌 Règles générales de l'en-tête

Toujours **aligné à droite** et * Toujours les éléments dans l’ordre :

1. 💬 Discussion badge (lien vers le GitHub Discussions)
2. GitHub stars badge (pour le dépôt courant)
3. ✨ lien vers la page Hero page du même language
4. Bascule de langue (FR ↔ EN)

- **Jamais** dans `README_arxiv.md`.
- **Zéro espace** entre la balise`<a>` et `<img>` des badges (prévenir le soulignement).
- **Toujours au début** du fichier.

### 🔷 2.1 En-tête pour le principal README (EN)

Utiliser ceci pour le `README.md` dans un dépôt InterIA :

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

### 🔶 2.2 En-tête pour le README_FR principal (FR)

Utiliser ceci pour `README_FR.md` :

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

### 2.3 🔷 En-tête pour le README Hero (EN)

Utiliser ceci pour `README_hero.md` :

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

### 🔶 2.4 En-tête pour le Hero README (FR)

Utiliser ceci pour `README_hero_FR.md` :

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

L'idée est :

- chaque README pointe vers le **Hero de sa langue** via ✨
- le dernier lien est toujours le **<sélecteur de langue** (FR ↔ EN)

---

## 🖥️ 3. Typographie & Blocs

### Gros titres

- Utiliser `#` puis `##`, rarement `###` (bannir les `####` – trop petits).

### Corps

- Texte clair, phrases courtes et pas de gras excessif.

### Éléments importants

- Utilisez les citations `> …` pour les clauses de non-responsabilité, les statuts ou les avertissements importants.
- Utilisez `---` (ligne horizontale) pour séparer les sections principales.
- Évitez d'utiliser trop souvent les styles gras/italique.

### ⚠️ **Blocs de codes** (```` ``` ````) dans un `bloc de code`

> Généralement, le *texte/code* est **encapsulé** par les fameux trois accents graves (`` ` ``) (backtick en anglais) ; \
> Il suffit qu'il y ait un ou plusieurs blocs de code pour briser l'affichage HTML.

- 💠 Pour éviter cela, **encapsulez** avec plus de \` que pour les **blocs de code à l'intérieur**. \
• Voir les deux chapitres Template README en mode `source` (il y a 4 \` afin d'éviter la brisure à la fin du bloc ```` ```bibtex ````).
- 💡 Cherchez **markdown** dans les *extensions* de votre navigateur (ou utilisez un **md viewer** en ligne).

<details><summary>

### 🛡️ Règle Anti-Casse Markdown InterIA

</summary>

Lorsqu’un bloc de code (```` ``` `````) doit contenir un autre bloc de code :

1. Toujours utiliser un "délimiteur de code" (fence) externe **d’un niveau supérieur** :
   - ````` ````md ````` pour l'extérieur
   - ```` ```bash ```` pour l'intérieur
2. Toujours fermer les blocs avec **la même séquence** qu’à l'ouverture.
3. Si un contenu risque de casser le rendu, utiliser :
   - soit les fences alternatifs `~~~`,
   - soit l’indentation `    ` (4 espaces).

Afin de garantir un rendu Markdown parfaitement stable (GitHub / GitLab / Pandoc / ChatGPT / IDE),
toute inclusion d’un *bloc de code contenant un autre bloc de code* doit utiliser l’une des 3 méthodes suivantes.

---

### ✔️ 1) Méthode classique — Fence externe plus long

````md
```bash
python script.py
```
````

- Le bloc externe utilise cinq backticks (`````).
- Le bloc interne en utilise trois (```).
- Aucune collision n’est possible.

⚠️ Certains éditeurs légers peuvent mal colorer,
mais **le rendu HTML final sera correct**.

---

### ✔️ 2) Méthode alternative — Fences `~~~` (tildes)

<!-- markdownlint-disable code-fence-style -->
~~~md
```bash
python script.py
```
~~~
<!-- markdownlint-enable code-fence-style -->

- Les *tildes* sont reconnues par tous les moteurs modernes.
- Elles permettent d’inclure des triple-backticks sans conflit.
- ✔ Sûr **tant qu’il n’y a pas de `~~~` dans le code interne**.

⚠️ Si le code interne contient **aussi** des `~~~`, cette méthode peut échouer.

---

### ✔️ 3) Méthode alternative — Indentation (4 espaces)

```md
    ```bash
    python script.py
    ```
```

- Indentation de **4 espaces** minimum.
- Rendu garanti sur *toutes* les plateformes.
- Moins élégant mais **infaillible** pour les contenus complexes.

---

### 🎯 Rappel important

Certaines séquences comme :

- \` \`\`\` \`
- ou (```` ``` ````)

ne doivent jamais apparaître **directement** dans un texte brut, car elles peuvent être interprétées comme début/fin d’un fence.

Toujours utiliser l’un des échappements suivants :

- entre fences externes :
  (```` ``` ````)

- ou en version échappée (sécurité maximale) :
  (\\\`\\\`\\\`)

Ces règles garantissent un rendu stable dans *tous* les cas
(GitHub, GitLab, ChatGPT, Pandoc, Obsidian, VSCode…).

</details>

---

## 🧩 4. Structure Canonique d’un README.md InterIA

Voici le template **officiel** recommandé pour les dépôts InterIA.

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

Fournir une entrée BibTeX (variantes FR & EN si besoin).

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
@misc{interia_exemple_2025_fr,
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

## 🌅 5. Structure Canonique d’un README Hero

Les README Hero sont des points d'entrée courts, de type « couverture », avec un aspect plus soigné, destinés à être utilisés comme pages d'accueil (et liés à partir de badges, de pages GitHub, etc.).

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

## 📁 6. Fichiers à **NE PAS** corporate-iser

Toujours garder les fichiers suivants **sans badge** :

- `README_arxiv.md`
- `main_arxiv.tex`
- `main_journal*.tex`
- `appendix/*.tex`
- `theorems/*.tex`
- version pour les journaux (PhD / Annals-like)

Celles-ci doivent rester aussi neutres et minimales que possible afin de respecter les normes académiques.

---

## 🔧 7. Palette & Identité

### Couleurs directrices

| Élément         | Couleur           | Usage                                    |
| --------------- | ----------------- | ---------------------------------------- |
| Bleu clair      | `#1e88e5`         | Badge Discussion                         |
| Bleu nuit       | `#0d47a1`         | Label background                         |
| Noir/Anthracite | par défaut GitHub | Titres, texte                            |
| `*`Emoji 💬     | invariant         | Identité InterIA (communication ouverte) |

`*` Est le symbole canonique pour InterIA « discussion ouverte ».

- Pas de branding agressif, pas de logos dans les PDF sauf si explicitement requis.

### Style LaTeX (optionnel)

Pour les documents PDF, utiliser :

- `\usepackage{libertinus}`
- titres sobres
- pas de logos colorés

---

## 📐 8. Lien (canonique) vers la **Proof Gallery**

À inclure dans tous les READMEs et hero :

```md
[🖼️ Proof Gallery](https://couret-interia.github.io/<repo>/#gallery)
```

Où `<repo>` est le nom du référentiel (par exemple, ``rh-analytic-framework-t1t4``).

Elle devient la **source canonique** pour :

- journaux de preuve
- audits λ
- schémas en grand format
- diaporamas T1′–T4

---

## 🧪 9. Intégration CI/CD

Conventions CI :

- `latex.yml` pour build PDF
- `pages.yml` pour GitHub Pages
- `linter.yml` optionnel pour Markdown

---

## 🧭 10. Évolution du style

Version du guide stylistique :

- **v1.0.0**

Les mises à jour futures (v1.1, v1.2, …) peuvent étendre :

- indications de couleurs adaptées au mode sombre,
- templates additionnels (ex. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`),
- Thèmes de documentation MkDocs ou Sphinx alignés sur ce style.

---
