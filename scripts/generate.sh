#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
docker run -it --rm -v $(pwd):/material:ro -v $(pwd)/out:/out ghcr.io/edinburghhacklab/hacklab-training:main /material /out $@
