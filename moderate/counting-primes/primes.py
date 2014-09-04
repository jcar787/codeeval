#!/usr/bin/env python
import sys

def is_prime(i):
    global primes
    if i == 0 or i == 1:
        return False
    if i == 2 or i == 3:
        return True
    if i%2==0 or i%3==0:
        return False
    for x in range(5, i):
        if i%x==0:
            return False
    primes.append(i)
    return True

test_cases = open(sys.argv[1], 'r')
primes = [2,3]
for test in test_cases:
    n,m = [int(x) for x in test.strip().split(',')]
    count = 0
    for i in range(n,m+1):
        if i in primes or is_prime(i):
            count += 1

    print count
test_cases.close()    
