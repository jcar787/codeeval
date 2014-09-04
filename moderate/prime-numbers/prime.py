#!/usr/bin/env python
import sys

def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
                                
    for i in range(3,n,2):
        if n%i == 0:
            return False
    return True
                                                                            
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n = int(test.strip())
    primes = [2,3]
    i = max(primes)
    if i > n:
        index = next(x[0] for x in enumerate(primes) if x[1] >= n)
        print ','.join(str(x) for x in primes[:index])
    elif i==n:
        print ','.join(str(x) for x in primes[:primes.index(n)+1])
    else:
        while i < n:
            if i in primes:
                i+=2
                continue
            elif is_prime(i):
                primes.append(i)
            i+=2
        print ','.join(str(x) for x in primes)
test_cases.close()
