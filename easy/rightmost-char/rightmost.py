#!/usr/bin/env python

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    phrase, letter = test.strip().split(',')
    for i in range(len(phrase)-1,-1, -1):
        if phrase[i] == letter:
            print i
            break
    else:
        print -1
