#!/usr/bin/python
import sys
import itertools
import copy

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input18.txt', 'r')
grid = []
n_steps = 100
size = 100
corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]

while True:
    line = f.readline().rstrip()
    if not line:
        break
    grid.append(map(lambda x: 0 if x == '.' else 1, list(line)))

for i, j in corners:
    grid[i][j] = 1
grid2 = copy.deepcopy(grid)
for s in range(n_steps):
    for i in range(size):
        for j in range(size):
            neighbors = list(itertools.chain(
                *map(lambda x: x[max(j - 1, 0):min(j + 2, size)], grid[max(i - 1, 0):min(i + 2, size)])))
            n_on = sum(neighbors) - (1 if grid[i][j] else 0)
            if (grid[i][j] and n_on not in [2, 3]) or (not grid[i][j] and n_on == 3):
                if part2 and grid[i][j] and (i, j) in corners:
                    continue
                grid2[i][j] = grid[i][j] ^ 1
    grid = copy.deepcopy(grid2)

print sum(map(sum, grid))
