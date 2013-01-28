#!/bin/sh
rm -rf _build
python regen.py
make html
