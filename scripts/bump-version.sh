#!/usr/bin/env bash
set -euxo pipefail

sed -i "s#getsentry/action-setup-venv@.*#getsentry/action-setup-venv@v$2#" README.md
