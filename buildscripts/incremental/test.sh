#!/bin/bash

source activate $CONDA_ENV

# Make sure any error below is reported as such
set -v -e

# Run test suite

python --version

if [ "$OPAQUE_POINTERS" == "yes" ]; then
    export LLVMLITE_ENABLE_OPAQUE_POINTERS=1
    echo "Testing with opaque pointers enabled"
else
    echo "Testing with opaque pointers disabled"
fi

if [ "$WHEEL" == "yes" ]; then
    cd dist
    python -m llvmlite.tests -v
else
    python runtests.py -v
fi

if [ "$RUN_COVERAGE" == "yes" ]; then coverage run runtests.py; fi
