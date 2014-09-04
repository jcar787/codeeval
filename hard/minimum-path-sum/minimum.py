#!/usr/bin/env python
import sys

def create_matrix(n, test):
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in test.readline().strip().split(',')])
    return matrix

def is_valid(x):
    if x < n:
        return True
    return False

def find_path(i, j):
    global path, mini
    if is_valid(i) and is_valid(j):
        path.append(matrix[i][j])
        find_path(i+1, j)
        find_path(i, j+1)

        if len(path) == n*2-1:
            if not mini:
                mini = sum(path)
            elif sum(path) < mini:
                mini = sum(path)
        path.pop()

def minimum():
    global path, mini
    path = []
    mini = None
    find_path(0,0)
    
test_cases = open(sys.argv[1], 'r')
n = int(test_cases.readline().strip())
global path, mini 
while n:
    matrix = create_matrix(n, test_cases)
    minimum()
    print mini
    tmp = test_cases.readline().strip()
    n = int(tmp) if tmp.isdigit() else None
test_cases.close()
