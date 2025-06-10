#!/usr/bin/env sh
cd "$(dirname "$0")/.."
docker run -it --rm -v $(pwd):/material:ro -v $(pwd)/out:/out ghcr.io/edinburghhacklab/hacklab-training:master /material /out $@
