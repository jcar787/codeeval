import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    one, two = test.strip().split(',')
    print one in (two+two)
    
test_cases.close()
