import sys
from operator import itemgetter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = test.strip().split()
    low = []
    st = set(nums)
    for i, n in enumerate(nums):
        if nums.count(n) == 1:
            low.append((n, i))
    
    if low:
        low.sort(key=itemgetter(0))
        print low[0][1]+1
    else:
        print 0
test_cases.close()
