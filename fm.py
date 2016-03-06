#!/usr/bin/env python
# This script is intentionally short, therefore many assumptions are made.

import os, sys

CONFIGS = (
    os.path.join(os.environ['HOME'], ".fastmenu"),
    "fastmenu.cfg",
)
SEP = '|'

if len(sys.argv) > 1 and sys.argv[1] == "--split":
    items = sys.stdin.readlines()
    if len(items) > 0:
        print(items[0].split(SEP)[1])
else:
    valid_cfg = [config for config in CONFIGS if os.path.exists(config)]
    if valid_cfg:
        cfg = dict([line.strip().split(SEP) for line in file(valid_cfg[0]) if line.strip()])
        longest = max([len(k) for k in cfg])
        for label, cmd in cfg.items():
            print("%s %s %s" % (label.ljust(longest), SEP, cmd))

sys.exit(0)
