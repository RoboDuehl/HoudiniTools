#!/bin/bash

for filename in /g/test/*.FBX; do
    hython hythonscript.py "/g/My Drive/Projects/Houdini/HipFiles/hython.hiplc" "$filename"
done
    