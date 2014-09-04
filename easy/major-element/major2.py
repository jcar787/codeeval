import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = [int(x) for x in test.strip().split(',')]
    dc = {}
    for x in lst:
        if dc.has_key(x):
            dc[x] += 1
        else:
            dc[x] = 1
    mx = max(dc.values()) 
    if  mx > len(lst)/2:
        for key in dc.keys():
            if mx == dc[key]:
                print key
                break
    else:
        print 'None'    

test_cases.close()
