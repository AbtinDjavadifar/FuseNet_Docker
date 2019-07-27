#!/usr/bin/env bash

CURRENT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )"
if [[ -z "$CURRENT_DIR" ]]; then
    CURRENT_DIR="/"
fi

while read requirement; do
    [ -z "$requirement" ] && continue
    echo "Installing $requirement"
    bash -c "conda install -y  $requirement"
done < "$CURRENT_DIR/conda-requirements.txt"

while read requirement; do
    [ -z "$requirement" ] && continue
    echo "Installing $requirement"
    bash -c "pip install $requirement"
done < "$CURRENT_DIR/requirements.txt"
