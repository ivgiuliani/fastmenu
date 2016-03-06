#!/usr/bin/env python

import os
import sys

CONFIGS = (
    os.path.join(os.environ['HOME'], ".fastmenu"),
    "fastmenu.cfg",
)


def load_config(config_file_path):
    return dict([line.strip().split("|") for line in file(config_file_path) if line.strip()])


def main(args):
    if len(args) > 1 and args[1] == "--exec":
        items = sys.stdin.readlines()
        if len(items) > 0:
            label, cmd = items[0].split("|")
            os.system(cmd.strip())
    else:
        valid_cfg = [config for config in CONFIGS if os.path.exists(config)]
        if not valid_cfg:
            print("No config file found.")
            return False
        cfg = load_config(valid_cfg[0])
        longest = max([len(k) for k in cfg])
        for k, v in cfg.items():
            print("%s | %s" % (k.ljust(longest), v))

    return True


if __name__ == "__main__":
    sys.exit(main(sys.argv))
