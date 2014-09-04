import sys
from operator import itemgetter
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums, total = test.strip().split(';')
    total = int(total)
    nums = [int(x) for x in nums.split(',')]
    acum = []
    for i, n in enumerate(nums):
        for j in nums[i+1:]:
            if n + j == total:
                acum.append((n,j))
    if acum:
        acum.sort(key=itemgetter(0))
        print ';'.join(map(lambda x: ','.join([str(i) for i in x])  , acum))
    else:
        print 'NULL'
test_cases.close()
