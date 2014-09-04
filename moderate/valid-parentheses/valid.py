#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    parentheses = []
    for p in test.strip():
        if p in ['(', '[', '{']:
            parentheses.append(p)
        elif parentheses:
            temp = parentheses.pop()
            if temp == '(' and p == ')' or \
                 temp == '[' and p == ']' or \
                 temp == '{' and p == '}':
               continue
            else:
                print False
                break

        else:
            print False
            break
    else:
        if parentheses:
            print False
        else:
            print True
test_cases.close()
