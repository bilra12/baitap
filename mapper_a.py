#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    match = re.match(r'\[(\w+ \w+ \d+ \d+):', line)
    if match:
        hour_slot = match.group(1)  # e.g. Dec 04 04
        print(f"{hour_slot}\t1")
