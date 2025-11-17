#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
InterIA / Couret–Unification
Versioning Validator

FR
---
Ce script vérifie qu'aucun fichier ou dossier "actif" ne contient
de numéro de version dans son nom (ex : "-v1.0", "v1.2-"),
conformément au guide VERSIONING_INTERIA.

Règles :
- Interdit (en dehors des exceptions) :
    - suffixes :   "name-v1.0.ext"
    - préfixes :   "v1.0-name.ext"
    - dossiers :   "module-v2/", "images-v1.1/"
- Ignorés :
    - le dossier racine "archives/" (et tout son contenu)
    - le répertoire .git, .github, etc.
- Exceptions :
    - fichiers ou dossiers explicitement autorisés
      via un fichier d'allowlist (par défaut : .interia_versioning_allowlist)

EN
---
This script checks that no "active" file or directory name
contains a version number pattern (e.g. "-v1.0", "v1.2-"),
according to the InterIA VERSIONING standard.

Rules:
- Forbidden (outside explicit exceptions):
    - suffixes:   "name-v1.0.ext"
    - prefixes:   "v1.0-name.ext"
    - dirs:       "module-v2/", "images-v1.1/"
- Ignored:
    - top-level "archives/" directory (and all of its content)
    - .git, .github, etc.
- Exceptions:
    - entries explicitly allowed in an allowlist file
      (default: .interia_versioning_allowlist)
"""

import argparse
import fnmatch
import os
import re
import sys
from typing import List, Tuple


# Regex pour détecter des motifs du type :
#   - "-v1", "-v1.0", "-v1.0.3"
#   - "v1-", "v1.0-name"
PATTERN_SUFFIX = re.compile(r"-v[0-9]+(\.[0-9]+)*")
PATTERN_PREFIX = re.compile(r"^v[0-9]+(\.[0-9]+)*-")


DEFAULT_ALLOWLIST = ".interia_versioning_allowlist"

IGNORED_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    ".mypy_cache",
    ".pytest_cache",
}


def load_allowlist(path: str) -> List[str]:
    """Charge une liste de patterns glob autorisés depuis un fichier (si présent)."""
    if not os.path.isfile(path):
        return []

    patterns: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # ignorer commentaires et lignes vides
            if not line or line.startswith("#"):
                continue
            patterns.append(line)
    return patterns


def is_allowed(rel_path: str, allow_patterns: List[str]) -> bool:
    """Retourne True si rel_path matche au moins un pattern d'allowlist."""
    for pattern in allow_patterns:
        if fnmatch.fnmatch(rel_path, pattern):
            return True
    return False


def has_version_pattern(name: str) -> bool:
    """Teste si un nom contient un motif de version interdit."""
    if PATTERN_SUFFIX.search(name):
        return True
    if PATTERN_PREFIX.search(name):
        return True
    return False


def scan_repo(root: str, allow_patterns: List[str]) -> List[Tuple[str, str]]:
    """
    Parcourt récursivement le dépôt et retourne une liste de violations.

    Chaque élément est un tuple (rel_path, kind) où kind est "file" ou "dir".
    """
    violations: List[Tuple[str, str]] = []

    root = os.path.abspath(root)
    for current_dir, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(current_dir, root)

        # Ignorer les dossiers techniques
        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORED_DIRS
        ]

        # Ignorer complètement archives/
        # (y compris archives/v1, archives/v2, etc.)
        # Si current_dir est déjà sous archives/, on ne descend pas plus loin.
        parts = rel_dir.split(os.sep)
        if parts[0] == "archives":
            # On n'explore pas plus profond
            dirnames[:] = []
            continue

        # Vérifier les noms de dossiers au niveau courant
        for d in list(dirnames):
            rel_path = os.path.join(rel_dir, d) if rel_dir != "." else d
            if is_allowed(rel_path, allow_patterns):
                continue
            if has_version_pattern(d):
                violations.append((rel_path, "dir"))

        # Vérifier les fichiers
        for fname in filenames:
            rel_path = os.path.join(rel_dir, fname) if rel_dir != "." else fname
            if is_allowed(rel_path, allow_patterns):
                continue
            if has_version_pattern(fname):
                violations.append((rel_path, "file"))

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check that no file/dir names contain version-like patterns (-vX.Y) "
                    "outside archives/ and explicit allowlist."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan (default: current directory).",
    )
    parser.add_argument(
        "--allowlist",
        default=DEFAULT_ALLOWLIST,
        help=f"Allowlist file path (default: {DEFAULT_ALLOWLIST}).",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: more compact output (still non-zero exit on violations).",
    )

    args = parser.parse_args()
    root = args.root
    allowlist_path = args.allowlist

    allow_patterns = load_allowlist(allowlist_path)
    violations = scan_repo(root, allow_patterns)

    if not violations:
        if not args.ci:
            print("✅ Versioning check passed: no forbidden version patterns found.")
        return 0

    # Affichage des violations
    print("❌ Versioning check failed. Forbidden version-like names detected:\n")
    for rel_path, kind in sorted(violations):
        print(f" - [{kind}] {rel_path}")

    print("\n💡 Rappel des règles InterIA :")
    print("  - Aucun suffixe '-vX.Y' ou préfixe 'vX.Y-' dans les noms actifs.")
    print("  - Déplacer les versions anciennes dans 'archives/'.")
    print("  - Pour les rares fichiers historiques, utiliser une allowlist : "
          f"{allowlist_path}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
