import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print max(test.split(), key=len)

test_cases.close()
