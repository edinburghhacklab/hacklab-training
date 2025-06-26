#!/usr/bin/env sh
set -euo pipefail

cd "$(dirname "$0")/.."
./scripts/generate.sh $@
xdg-open out/
