#!/bin/bash

set -eu

dir=$1
url=$2
path=${url##*/}
contents=${path%_*}
level=${path#*_}
mkdir -p $dir/$contents/$level && cd $dir/$contents/$level
touch main.py && oj d $url
code .
exec $SHELL -L 
