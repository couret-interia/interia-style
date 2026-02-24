# 📦 Guide de Versioning InterIA (FR)

**Organisation : `couret-interia` — Standard officiel**

Ce guide définit les règles **communes à tous les dépôts** de l’organisation InterIA.
L’objectif est d’assurer une structure propre, stable, lisible, et compatible avec CI/CD.

---

## 🎯 Objectif

Éviter la multiplication de fichiers et dossiers avec des suffixes `-vX.Y`, tout en permettant
la préservation historique **lorsqu’elle est utile**.

Le dépôt doit rester :

- clair,
- stable dans ses imports,
- simple à maintenir,
- git-friendly.

---

## 📐 Règles Officielles

### 1) 🚫 **Aucun numéro de version dans les noms (règle absolue)**

Les fichiers actifs, maintenus ou utilisés dans le projet **ne doivent jamais contenir** :

- de suffixe `-vX.Y`
- de préfixe `vX.Y-`
- de dossiers versionnés (ex : `module-v3/`)

Cela garantit que :

- la version courante est toujours évidente,
- les imports / includes ne changent jamais,
- la CI/CD reste stable,
- la structure est propre.

**Exemples (obligatoire)** :

```

logo.svg             ← OK (version courante)
script.js            ← OK
script-v1.0.js       ← NON (à archiver)
README-v1.0.md       ← NON (à archiver)

```

---

### 2) 📁 Archives historiques (optionnel, contrôlé)

Pour conserver certaines versions utiles :

- créer un dossier `archives` **à la racine de chaque dépôt**.

Structure recommandée :

```

archives/
├── v1/
├── v2/
└── v3/

```

Chaque version contient les fichiers en l’état :

```

archives/v1/main_arxiv-v1.0.0.tex
archives/v1/Makefile-v1.2
archives/v1/scripts/make_arxiv-v1.0.sh

```

👉 L’usage de `/archives/` est **exceptionnel**, jamais automatique.

---

### 3) 🗝️ Fichiers “historiques pivots” autorisés

Certains fichiers méritent de rester visibles dans les dossiers actifs :

- concepts fondateurs,
- brouillons graphiques importants,
- styles expérimentaux,
- documents de conception significatifs.

Dans ce cas :
✔ ils peuvent garder un suffixe `-vX.Y`
✔ ils doivent être peu nombreux
✔ ils doivent être clairement identifiés comme historiques

Exemples :

```

branding/logo-historique-v0.9.svg
frameworks/colors-experimental-v2.1.json

```

---

### 4) 🚫 Ne jamais versionner les dossiers

Git assure déjà l’historique.
Donc :

- pas de `appendix-v3/`
- pas de `images-v2/`
- pas de `latex-v1.1/`

---

## ✔️ Résumé en une phrase

**Aucun fichier ou dossier actif ne doit contenir un suffixe `-vX.Y`; les anciennes versions vont dans `/archives/`, et seules quelques ressources historiques peuvent garder un suffixe.**

---

## 💾 Numérotation des versions (tags Git)

La version d’un dépôt InterIA doit **toujours être dans les tags Git**, jamais dans les noms de fichiers.

Format officiel :

```

MAJOR.MINOR.PATCH

```

- MAJOR → rupture ou refonte majeure
- MINOR → nouvelle fonctionnalité compatible
- PATCH → correction ou amélioration mineure

Versions préliminaires :

```

1.0.0-alpha.1
1.0.0-beta.2
1.0.0-rc.1

```

Les tags Git doivent être utilisés pour :

- releases GitHub,
- packaging,
- Zenodo DOI,
- citations académiques,
- compatibilité CI/CD.

---

## 🔧 Validation automatique (script InterIA)

Pour garantir le respect de ces règles dans tous les dépôts `couret-interia`,
un script de validation est fourni :

- Fichier : `tools/check_versioning.py`
- Fonction : vérifier qu’aucun fichier ou dossier **actif** ne contient de motif de version
  du type `-vX.Y` ou `vX.Y-`, en excluant :
  - le dossier `archives/` (et son contenu),
  - certains dossiers techniques (`.git`, `.github`, `__pycache__`, etc.),
  - les chemins explicitement autorisés via une *allowlist*.

### Usage en local

Depuis la racine d’un dépôt :

```bash
python tools/check_versioning.py --root .
```

Retour :

- code de sortie `0` → ✅ aucune violation détectée,
- code de sortie `1` → ❌ au moins un fichier/dossier contient un motif interdit.

### Allowlist : `.interia_versioning_allowlist`

Pour quelques fichiers *historiques* jugés importants, il est possible de les autoriser
explicitement via un fichier `.interia_versioning_allowlist` à la racine du dépôt.

Exemple :

```txt
# Fichiers / dossiers autorisés à contenir -vX.Y
branding/logo-historique-v0.9.svg
frameworks/colors-experimental-v2.1.json
legacy/**/prototype-v1.0.*
```

Tout chemin non listé et contenant `-vX.Y` sera considéré comme une violation.

### Intégration CI (GitHub Actions)

Il est recommandé de brancher le script dans la CI de chaque dépôt :

```yaml
name: Versioning Check

on:
  push:
  pull_request:

jobs:
  versioning:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run versioning validator
        run: |
          python tools/check_versioning.py --root . --ci
```

Ainsi, **aucun nouveau fichier ou dossier** ne pourra être introduit avec un suffixe `-vX.Y`
sans être explicitement autorisé.

## 📎 Fin du document — Ce standard s’applique à *tous* les dépôts InterIA
