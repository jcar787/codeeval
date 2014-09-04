import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = map(int, test.strip().split())
    n = lst[0]
    i = 1
    for l in lst[1:]:
        if n == l:
            i += 1
        else:
            print i, n,
            n = l
            i = 1            
    print i, n
test_cases.close()
