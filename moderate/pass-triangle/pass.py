#!/usr/bin/env python
import sys

def create_matrix():
    matrix = []
    f = open(sys.argv[1], 'r')
    for l in f:
        matrix.append([int(x) for x in l.strip().split()])
    return matrix

def is_col_valid(i):
    if i < len(matrix):
        return True
    return False

def is_row_valid(i,j):
    if j < len(matrix[i]):
        return True
    return False

def pass_triangle(i, j):
    global maxi, path
    
    if is_col_valid(i) and is_row_valid(i,j):
        path.append(matrix[i][j])
        pass_triangle(i+1, j)
        pass_triangle(i+1, j+1)
        if len(path) == len(matrix):
            if not maxi or sum(path) > maxi:
                maxi = sum(path)
        path.pop()

def get_max():
    global maxi, path
    maxi = None
    path = []
    pass_triangle(0,0)
    return maxi
        

matrix = create_matrix()
global maxi
global path
print get_max()
