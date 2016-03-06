#!/bin/bash
cd "$(dirname "$0")"
./fm.py | (dmenu -i -l `./fm.py | wc -l`) | ./fm.py --split | ${SHELL:-"/bin/sh"} &
