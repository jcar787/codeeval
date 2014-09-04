#!/usr/bin/env python
import sys 
test_cases = open(sys.argv[1], 'r')
nums = [0,1,1,2]
while len(nums) < 3000000:
    nums += [(1<<x)%4 for x in nums]
for test in test_cases:
    n = int(test.strip())
    print nums[n]
test_cases.close()
