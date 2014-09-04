#!/usr/bin/env python
import sys

f = open(sys.argv[1], 'r')
for test in f:
    number, pattern = test.strip().split()
    sm = True if pattern.find('+') > -1 else False
    index = pattern.find('+') if sm else pattern.find('-')
    total = int(number[:index]) + int(number[index:]) if sm else int(number[:index]) - int(number[index:])
    print total
f.close()
