#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
./scripts/generate.sh $@
xdg-open out/
