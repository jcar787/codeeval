import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    chrs = []
    for i,x in enumerate(test):
        if x in test[i+1:] or x in chrs:
            chrs.append(x)
        else:
            print x
            break
test_cases.close()
