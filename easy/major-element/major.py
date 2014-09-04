import sys
from collections import Counter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = [int(x) for x in test.strip().split(',')]
    c = Counter(lst)
    l = len(lst)
    mc = c.most_common(1)
    if mc[0][1] > l/2:
        print mc[0][0]
    else:
        print 'None'    

test_cases.close()
