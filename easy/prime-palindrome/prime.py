def is_prime(n):
    if n == 0 or n == 1 or n%2==0:
        return False
    if n == 2:
        return True
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True
    
for i in range(999,0,-2):
    if is_prime(i) and str(i) == str(i)[::-1]:
        print i
        break
