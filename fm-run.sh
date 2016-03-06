#!/bin/bash
./fm.py | (dmenu -i -l `./fm.py | wc -l`) | ./fm.py --split | ${SHELL:-"/bin/sh"} &
