import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = map(lambda x: int(x.split(',')[1]), test.strip()[:-1].split(';'))
    lst.sort()
    nw =[lst[0]]
    for i, d in enumerate(lst):
        if i+1 == len(lst):
            break
        nw.append(lst[i+1]-d)
        
    print ','.join(map(str,nw))

test_cases.close()
