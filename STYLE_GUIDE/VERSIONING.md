# 📦 InterIA Versioning Guide (EN)
**Organization: `couret-interia` — Official Standard**

This guide defines the **global rules** applied across all repositories in the InterIA ecosystem.
The goal is to keep repositories clean, stable, predictable and CI-friendly.

---

# 🎯 Objective

Avoid the proliferation of `-vX.Y` suffixes while preserving useful historical material when needed.

The structure must remain:
- clean
- stable for imports
- easy to maintain
- compatible with Git & CI/CD

---

# 📐 Official Rules

## 1) 🚫 **No version numbers in filenames or directory names (absolute rule)**

Active or maintained files **must never include**:
- suffixes like `-vX.Y`
- prefixes like `vX.Y-`
- versioned folders (e.g. `module-v3/`)

This ensures:
- the current version is always obvious
- imports never break
- CI remains stable
- the repo stays clean

**Examples (mandatory):**
```

logo.svg            ← OK (current)
script.js           ← OK
script-v1.0.js      ← NO (must go to archives)
README-v1.0.md      ← NO (must go to archives)

```

---

## 2) 📁 Historical archives (optional, controlled)

To preserve past versions when meaningful:
- create an `archives` directory **at the root of the repository**.

Recommended structure:
```

archives/
├── v1/
├── v2/
└── v3/

```

Example contents:
```

archives/v1/main_arxiv-v1.0.0.tex
archives/v1/Makefile-v1.2
archives/v1/scripts/make_arxiv-v1.0.sh

```

Use of `/archives/` is **exceptional**, never automatic.

---

## 3) 🗝️ Allowed “historical pivot files”

Some files are important enough to keep visible outside `/archives/`:
- early design concepts
- key prototypes
- important drafts
- major experimental styles

These files may retain a version suffix:
```

branding/logo-historic-v0.9.svg
frameworks/colors-experimental-v2.1.json

```

---

## 4) 🚫 Never version directories

Git already tracks history.
Avoid:
- `appendix-v3/`
- `images-v2/`
- `latex-v1.1/`

---

# ✔️ Summary in one sentence

**No active file or folder may contain a `-vX.Y` suffix; old versions belong in `/archives/`, and only a few historical resources may retain version numbers.**

---

# 💾 Repository version numbers (Git tags only)

Repository versions must always be handled using Git tags, never filenames.

Format:
```

MAJOR.MINOR.PATCH

```

Example prereleases:
```

1.0.0-alpha.1
1.0.0-beta.2
1.0.0-rc.1

```

Git tags are used for:
- GitHub releases
- Zenodo DOI
- CITATION.cff
- software packaging
- CI/CD compatibility

---


# 🔧 Automatic validation (InterIA script)

To enforce these rules consistently across all `couret-interia` repositories,
a dedicated validator script is provided:

- File: `tools/check_versioning.py`
- Purpose: ensure that no **active** file or directory name contains a version-like
  pattern such as `-vX.Y` or `vX.Y-`, while ignoring:
  - the `archives/` directory (and its contents),
  - technical directories (`.git`, `.github`, `__pycache__`, etc.),
  - explicitly allowed paths via an *allowlist*.

## Local usage

From the repository root:

```bash
python tools/check_versioning.py --root .
```

Exit code:

* `0` → ✅ no violations detected
* `1` → ❌ at least one file or directory name contains a forbidden pattern

## Allowlist: `.interia_versioning_allowlist`

For a few important *historical* files, you may explicitly allow them via an
`.interia_versioning_allowlist` file at the repository root.

Example:

```txt
# Files / directories allowed to contain -vX.Y
branding/logo-historic-v0.9.svg
frameworks/colors-experimental-v2.1.json
legacy/**/prototype-v1.0.*
```

Any path not listed and containing `-vX.Y` will be treated as a violation.

## CI Integration (GitHub Actions)

It is recommended to plug the script into each repository’s CI:

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

This ensures that **no new files or directories** using a `-vX.Y` suffix can be added
without being explicitly whitelisted.

# 📎 End of document — This standard applies to *all* InterIA repositories.
