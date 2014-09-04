import sys, re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word, search = test.strip().split(',')
    search = search.replace('*', '[\w\W]*')
    print 'true' if re.search(search, word) else 'false'
test_cases.close()
