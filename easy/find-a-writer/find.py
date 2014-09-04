import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    letters, keys = test.strip().split('|')
    keys = [int(i)-1 for i in keys.split()]
    res = ''
    for key in keys:
        res += letters[key]
    print res
test_cases.close()
