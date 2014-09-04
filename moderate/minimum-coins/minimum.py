import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    change = int(test.strip())
    coins = 0
    while change != 0:
        if change > 4:
            coins += 1
            change -= 5
        elif change > 2:
            coins += 1
            change -= 3
        else:
            coins += 1
            change -= 1
    print coins
test_cases.close()
