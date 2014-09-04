import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    st1, st2 = map(set, map(lambda x: x.split(','), test.strip().split(';')))
    print ','.join([str(x) for x in sorted(map(int,st1&st2))])

test_cases.close()
