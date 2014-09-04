import sys
import re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word, search = test.strip().split(',')
    if re.search('{0}$'.format(search), word):
        print 1
    else:
        print 0
test_cases.close()
