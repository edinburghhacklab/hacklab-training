generate:
    docker run -it --rm -v $(pwd):/material:ro -v $(pwd)/out:/out ghcr.io/edinburghhacklab/hacklab-training:master /material /out

open: generate
    xdg-open ./out/index.html
