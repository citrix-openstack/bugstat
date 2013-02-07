#!/bin/bash
set -eux

TEMPDIR=`mktemp -d`
python tools/makebugstat.py "$TEMPDIR" > bugreport/main_report.md
rm -rf "$TEMPDIR"
