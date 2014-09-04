import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print 1 if int(test.strip())%2 == 0 else 0
test_cases.close()
