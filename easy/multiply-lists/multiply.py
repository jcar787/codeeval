import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    m1,m2 = test.split('|')
    m1 = map(int, m1.split())
    m2 = map(int, m2.split())
    for i,m in enumerate(m1):
        print m*m2[i],
    print
test_cases.close()
