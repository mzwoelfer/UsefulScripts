#!/bin/bash

docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex document.md -o document.pdf

