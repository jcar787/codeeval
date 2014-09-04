import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print ' '.join(x for x in test.strip().split()[::-2])

test_cases.close()
