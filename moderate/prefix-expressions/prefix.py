#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    vals = test.strip().split()
    nums = []; ops = []
    for val in vals:
        if val.isdigit():
            nums.append(val)
        else:
            ops.append(val)
        while len(nums) > 1 and len(ops) > 0:
            nums.append(eval('{0}{1}{2}'.format(nums.pop(), ops.pop(), nums.pop())))

print nums[0]

test_cases.close()
