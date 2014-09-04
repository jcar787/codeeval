import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print ' '.join(map(lambda x: x[0].upper()+x[1:], test.split()))

test_cases.close()
