import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print  ','.join(str(x) for x in sorted(set(int(i) for i in test.strip().split(','))))
test_cases.close()
