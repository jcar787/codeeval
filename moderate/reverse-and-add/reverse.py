#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n = test.strip()
    x = 0
    if n == n[::-1]:
        print 1, n
    else:
        i = 0
        for i in range(100):
            x = int(n) + int(n[::-1])
            if str(x) == str(x)[::-1]:
                break
            else:
                n = str(x)

        print i+1, x

