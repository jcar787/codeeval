import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print bin(int(test.strip())).replace('0b','')
test_cases.close()
