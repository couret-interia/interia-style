# Makefile – Couret–InterIA standard
# Versioning / style tooling

PYTHON ?= python3

.PHONY: check-versioning
check-versioning:
	@echo "🔎 Running InterIA versioning check..."
	@$(PYTHON) tools/check_versioning.py

# Optionnel : regrouper plusieurs checks dans une cible "lint"
# Optional: group several checks in a “lint” target
.PHONY: lint
lint: check-versioning
	@echo "✅ All lint checks passed."
