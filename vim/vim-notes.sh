#!/bin/bash

noteFile="$HOME/notes/note-$(date +%d-%m-%Y).md"

if [ ! -f $noteFile ]; then
    echo "# Notes for $(date +%d-%m-%Y)" > $noteFile
fi

vim -c "norm Go" \
    -c "norm Go## $(date +%H:%M)" \
    -c "norm G2o" \
    -c "norm zz" \
    -c "startinsert" $noteFile
