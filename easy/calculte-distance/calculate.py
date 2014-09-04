import sys
from math import sqrt
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = map(int, test.strip().replace('(','').replace(')','').replace(',','').split())
    print int(sqrt((nums[2]-nums[0])**2+(nums[3]-nums[1])**2))
test_cases.close()
