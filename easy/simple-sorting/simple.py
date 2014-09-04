import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print ' '.join('{:.3f}'.format(i) for i in sorted([float(x) for x in test.strip().split()]))
test_cases.close()
