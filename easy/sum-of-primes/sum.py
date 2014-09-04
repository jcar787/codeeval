#!/usr/bin/env python

def is_prime(n):
    if n == 0 or n == 1 or n%2 == 0:
        return False
    if n == 3:
        return True
    for i in range(3,n,2):
        if n%i == 0:
            return False
    return True


i = 1; res = 2; j = 3
while i<1000:
    if is_prime(j):
        print i,'->',j,' ',
        i += 1
        res += j
    j += 2    
print res
