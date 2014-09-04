#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers, swaps = test.strip().split(':')
    numbers = numbers.strip().split()
    swaps = swaps.strip().split(',')
    for swap in swaps:
        first, last = [int(x) for x in swap.strip().split('-')]
        numbers[first], numbers[last] = numbers[last], numbers[first]

    print ' '.join(numbers)

test_cases.close()
