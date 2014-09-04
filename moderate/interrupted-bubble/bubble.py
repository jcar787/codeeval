#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = [int(x) for x in test.split('|')[0].split()]
    lst_sorted = sorted(lst)
    t = int(test.split('|')[1])
    x = 0
    while x < t:
        for i in range(len(lst)-1):
            if lst_sorted == lst:
                break
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        x += 1
    print ' '.join(str(x) for x in lst)
test_cases.close()    
