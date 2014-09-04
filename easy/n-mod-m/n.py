import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n,m = map(int, test.strip().split(','))
    if m > n:
        print n
        continue
    elif n == m:
        print 0
        continue
    
    i = 1
    while True:
        rs = n - (m*i)
        if rs < m:
            print rs
            break
        elif rs == m:
            print 0
            break
        i += 1

test_cases.close()
