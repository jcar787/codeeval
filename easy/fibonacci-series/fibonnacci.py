#!/usr/bin/env python
import sys

def fib(n):
    return n if n<2 else fib(n-1) + fib(n-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    f = int(test.strip())
    print fib(f)
test_cases.close()
