# AGENTS.md

`getsentry/action-setup-venv` is a composite GitHub Action (`action.yml`) that sets up Python, creates a venv, and caches it.

## Commands

- Test: the `Self Test` workflow (`.github/workflows/self-test.yml`) runs the action on pull requests and on pushes to `main` and `test-me-*` branches. There is no local test command.
- Release: run the `Release` workflow (`.github/workflows/release.yml`) with a version. Craft runs `scripts/bump-version.sh`, which rewrites the version in README.

## Invariants

- `scripts/bump-version.sh` replaces everything after `getsentry/action-setup-venv@` to the end of the line in `README.md`. Do not put that string in README prose or add trailing comments to those `uses:` lines.
- `action.yml` inputs and outputs are the public API. Document each one in the README inputs and outputs tables.

## Docs

- User docs: `README.md`.
