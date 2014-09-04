import sys
test_cases = open(sys.argv[1], 'r')
digits = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
for test in test_cases:
    result = ''
    for x in test.strip():
        if x.isdigit():
            result += x
        else:
            result += digits[x] if x in digits else ''
    print result if result else 'NONE'
test_cases.close()
