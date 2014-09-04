import sys

global mx

def set_max(lst):
    global mx
    for i in range(1,len(lst)+1):
        for j in range(len(lst)):
            if lst[j:i]:
                mx = max(sum(lst[j:i]), mx)
        
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = map(int, test.strip().split(','))
    mx = sum(lst)
    set_max(lst)
    print mx
test_cases.close()
