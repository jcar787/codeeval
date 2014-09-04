import sys
test_cases = open(sys.argv[1], 'r')
dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
for test in test_cases:
    print ''.join(map(lambda x: dic[x], test.strip().split(';')))
test_cases.close()
