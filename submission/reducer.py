#!/usr/bin/env python
import sys

current_word = None
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        word, count = line.split('\\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        total += count
    else:
        if current_word is not None:
            print('%s\\t%s' % (current_word, total))
        current_word = word
        total = count

if current_word is not None:
    print('%s\\t%s' % (current_word, total))
