#!/usr/bin/env python
import sys 

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    zeros = test.strip().split()
    result = ''
    for i in range(0, len(zeros), 2):
        if zeros[i] == '0':
            result += zeros[i+1]
        else:
            result += zeros[i+1].replace('0', '1')
    print int(result, base=2)
test_cases.close()
