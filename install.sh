#!/bin/bash

if [ $# -eq 0 ]; then
    echo "please specify install directory."
    exit 1
fi

if [ ! -d "$1" ]; then
    mkdir -p "$1"
fi
cp -r dic $1
