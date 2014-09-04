#!/usr/bin/env python
import sys

global n, m

def has_mine(point, x, y):
    if not is_out(x,y) and field[x][y] == '*':
        return True
    return False

def is_out(x, y):
    global n, m
    if x == -1 or x == n  or y == -1 or y == m:
        return True
    return False

def get_mine_total(field, x, y):
    global n, m
    res = 0
    if has_mine(field, x+1, y):
        res += 1
    if has_mine(field, x-1, y):
        res += 1
    if has_mine(field, x, y+1):
        res += 1
    if has_mine(field, x, y-1):
        res += 1
    if has_mine(field, x+1, y+1):
        res += 1
    if has_mine(field, x+1, y-1):
        res += 1
    if has_mine(field, x-1, y+1):
        res += 1
    if has_mine(field, x-1, y-1):
        res += 1
    return res

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    global n, m
    nm, raw_field = test.strip().split(';')
    n,m = [int(x) for x in nm.split(',')]
    field = []
    for i in range(n):
        field.append([raw_field[i*m+x] for x in range(m)])

    for x in range(n):
        for y in range(m):
            if field[x][y] == '*':
                sys.stdout.write(str(field[x][y]))
                continue
            field[x][y] = get_mine_total(field, x, y)
            sys.stdout.write(str(field[x][y]))
    print
    sys.stdout.flush()
test_cases.close()
