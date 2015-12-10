#!/usr/bin/python
import sys

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input6.txt', 'r')
total = 0
grid = [[0 for x in range(1000)] for y in range(1000)]


def turnon(i, j):
    grid[i][j] = grid[i][j] + 1 if part2 else 1


def turnoff(i, j):
    grid[i][j] = max(grid[i][j] - 1, 0) if part2 else 0


def toggle(i, j):
    grid[i][j] = grid[i][j] + 2 if part2 else grid[i][j] ^ 1


while True:
    line = f.readline().rstrip()
    if not line:
        print sum(map(sum, grid))
        break
    line = line.replace('turn ', 'turn')  # normalizes amount of arguments
    print line  # This is the slowest script so far due to O(n^2); printing just so user knows it's running
    action, ia_ja, through, ib_jb = line.split(' ')
    ia, ja = map(lambda x: int(x), ia_ja.split(','))
    ib, jb = map(lambda x: int(x), ib_jb.split(','))
    for i in range(ia, ib + 1):
        for j in range(ja, jb + 1):
            eval("%s(i,j)" % action)
