#!/usr/bin/env python

import sys
test_cases = open(sys.argv[1], 'r')
founded = set([1])
repeated = set()
for test in test_cases:
    number = test.strip()
    lst_numbers = []
    found = False
    repeat = False
    if number in founded:
        found = True
        
    while not found and not repeat:
        numbers = [int(x) for x in number]
        total = 0
        for x in numbers:
            total += x ** 2

        if total in founded:
            found = True
            founded.update(lst_numbers)
        elif total in repeated or total in lst_numbers:
            repeat = True
            repeated.update(lst_numbers)
        else:
            lst_numbers.append(total)
            number = str(total)

    if found:
        print 1
    elif repeat:
        print 0 
