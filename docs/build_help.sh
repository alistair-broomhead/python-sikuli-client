#!/bin/sh
make clean
python regen.py
make html
if [ $? = 0 ]; then
    # If the build is successful, add everything except for the source
    # directory, which should be managed manually
    set DOCSDIR=docs/html
    git add $DOCSDIR/*
    git add $DOCSDIR/_sources
    git add $DOCSDIR/_static
    git add $DOCSDIR/doctrees
else
    exit $?
fi
