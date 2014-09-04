#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
longest = []
cnt = int(test_cases.readline().strip())
for n in range(cnt):
    longest.append(test_cases.readline().strip())
for test in test_cases:
    i = longest.index(min(longest, key=len))
    if len(test.strip()) > len(longest[i]):
        longest[i] = test.strip()
print '\n'.join(sorted(longest, key=len, reverse=True))
test_cases.close()
