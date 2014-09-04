#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words, pos = test.split(';')[0].split(), [int(x) for x in test.split(';')[1].split()]
    db = {} 
    
    for i, ps in enumerate(pos):
        db[ps] = words[i]

    for i in range(1,len(words)+1):
        if not i in db.keys():
            db[i] = words[-1]
            break
    print ' '.join(db.values())
test_cases.close()    
