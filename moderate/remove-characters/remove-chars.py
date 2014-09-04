#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.split(',')
    line[1] = line[1].strip()
    for char in line[1]:
        line[0] = line[0].replace(char, '')
    print line[0]
test_cases.close()    
