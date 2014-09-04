import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    bits = map(int,test.split(','))
    print 'true' if (bits[0]>>bits[1]-1)&1 == (bits[0]>>bits[2]-1)&1 else 'false'
test_cases.close()
