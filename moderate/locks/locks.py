#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n, m = [int(x) for x in test.strip().split()]
    doors = [True] * n
    for i in range(m-1):
        for j in range(1,n,2):
            doors[j] = False
        for j in range(2,n,3):
            doors[j] = not doors[j]
    doors[-1] = not doors[-1]
    print sum(doors)
test_cases.close()    
