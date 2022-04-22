#!/bin/bash

set -eu

contest=$1
atcoder-tools gen $contest --workspace=/Users/kokiyasuda/program/atcoder --lang=python --without-login
cd ./$1/A
code .
exec $SHELL -L 