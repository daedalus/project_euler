#!/bin/bash
set -x
N=$1
git add p$N.py; git commit p$N.py lib/math.py lib/strings.py -m "add p$N.py"; git push
