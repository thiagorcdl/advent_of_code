#!/usr/bin/python
import sys

f = open('./input6.txt', 'r')
total = 0
grid = [[0 for x in range(1000)] for y in range(1000)]

def turnon(i, j):
    grid[i][j] += 1

def turnoff(i, j):
    grid[i][j] -= 1
    grid[i][j] = max(grid[i][j], 0)

def toggle(i, j):
    grid[i][j] += 2

while True:
    line = f.readline().rstrip()
    if not line:
        print sum(map(sum, grid))
        break
    print line
    action, ia_ja, through, ib_jb = line.split(' ')
    ia, ja = map(lambda x: int(x), ia_ja.split(','))
    ib, jb = map(lambda x: int(x), ib_jb.split(','))
    for i in range(ia,ib+1):
        for j in range(ja, jb+1):
            eval("%s(i,j)" % action)
