#!/usr/bin/env python
# This script is intentionally short, therefore many assumptions are made.

import os, sys

CONFIGS = (
    os.path.join(os.environ['HOME'], ".fastmenu"),
    "fastmenu.cfg",
)

if len(sys.argv) > 1 and sys.argv[1] == "--exec":
    items = sys.stdin.readlines()
    if len(items) > 0:
        os.system(items[0].split("|")[1])
else:
    valid_cfg = [config for config in CONFIGS if os.path.exists(config)]
    if valid_cfg:
        cfg = dict([line.strip().split("|") for line in file(valid_cfg[0]) if line.strip()])
        longest = max([len(k) for k in cfg])
        for label, cmd in cfg.items():
            print("%s | %s" % (label.ljust(longest), cmd))

sys.exit(0)
