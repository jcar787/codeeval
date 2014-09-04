import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    num = test.strip()
    dig = len(num)
    print True if sum(map(lambda x: int(x)**dig, num)) == int(num) else False       

test_cases.close()
