import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.strip().split(';')
    lst = [int(x) for x in line[1].split(',')]
    for i, ele in enumerate(lst):
        if ele in lst[i+1:]:
            print ele
            break

test_cases.close()
