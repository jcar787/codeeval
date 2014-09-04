import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    vals = test.strip().split()
    i, vals = int(vals[-1]), vals[:-1]
    if len(vals) < i:
        continue
    print vals[-i]
test_cases.close()
