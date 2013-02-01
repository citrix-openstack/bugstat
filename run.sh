#!/bin/bash
set -eux

TEMPDIR=`mktemp -d`
python tools/makebugstat.py "$TEMPDIR" > bugreport/README.md
rm -rf "$TEMPDIR"
