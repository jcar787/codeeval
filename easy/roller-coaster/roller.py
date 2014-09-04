#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    result = ''
    sentence = test.strip()
    up = True
    for i in range(len(sentence)):
        if not sentence[i].isalpha():
            result += sentence[i]
        elif up:
            result += sentence[i].upper()
            up = False
        else:
            result += sentence[i].lower()
            up = True
    print result
test_cases.close()
