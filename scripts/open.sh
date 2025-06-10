#!/usr/bin/env sh
cd "$(dirname "$0")/.."
./scripts/generate.sh $@
xdg-open out/
