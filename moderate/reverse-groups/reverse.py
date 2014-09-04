#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst, k = test.strip().split(';')
    k = int(k)
    lst = lst.strip().split(',')
    for i in range(0,len(lst),k):
        if i+k >= len(lst):
            break
        j=0
        while j < k//2:
            lst[i+j], lst[i+k-1-j] = lst[i+k-1-j], lst[i+j]
            j+=k
    print ','.join(lst)
test_cases.close()
