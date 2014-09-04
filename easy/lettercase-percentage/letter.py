#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    total = len(test.strip())
    l = sum([1 for x in test.strip() if x.islower()])
    u = total - l
    print 'lowercase: {0:.2f} uppercase: {1:.2f}'.format(float(l)/total*100, 
                                                        float(u)/total*100)
test_cases.close()    
