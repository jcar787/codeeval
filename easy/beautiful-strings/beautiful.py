import sys, string
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip().lower()
    cnt = []; val = 26
    for x in string.lowercase:
        if test.count(x) > 0:
            cnt.append(test.count(x))
        if(sum(cnt) == len(test)):
            break
    cnt.sort(reverse=True)
    for i,c in enumerate(cnt):
        cnt[i] *= val
        val -= 1
    print sum(cnt)
test_cases.close()
