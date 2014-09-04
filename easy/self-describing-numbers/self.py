import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i,x in enumerate(test.strip()):
        if test.count(str(i)) != int(x):
            print 0
            break
    else:
        print 1
test_cases.close()
