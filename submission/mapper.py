#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.lower()
    line = re.sub(r'[^a-z0-9\\s]', ' ', line)
    for word in line.split():
        if word:
            print('%s\\t1' % word)
