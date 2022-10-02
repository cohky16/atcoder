#!/bin/bash

set -eu

levelList="abcdef"
url=$1
contest=${url##*/}
path="/tasks/$contest"
maxLevel=$2
for i in `seq ${maxLevel}`
do
  level=$(echo $levelList | cut -c $i)
  dir=./$contest/$level
  mkdir -p $dir && cd $dir
  touch main.py && oj d "${url}${path}_${level}"
  cd ../../
done

cd ./$contest/a
code .
exec $SHELL -L
