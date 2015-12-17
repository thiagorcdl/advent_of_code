#!/usr/bin/python
import re
import sys

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input15.txt', 'r').read()
pattern = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
ingr = []
[ingr.append(map(int, [cap, dur, flav, tex, cal])) for name, cap, dur, flav, tex, cal in re.findall(pattern, f)]
recipe = [0, 0, 0, 0]

best = 0
for i in reversed(range(101)):
    recipe[0] = i
    for j in range(100-i):
        recipe[1] = j
        for k in range(100-i-j):
            recipe[2] = k
            recipe[3] = 100-i-j-k
            if part2 and sum([ingr[x][4] * recipe[x] for x in range(4)]) != 500:
                continue
            cap = max(sum([ingr[x][0] * recipe[x] for x in range(4)]), 0)
            dur = max(sum([ingr[x][1] * recipe[x] for x in range(4)]), 0)
            flav = max(sum([ingr[x][2] * recipe[x] for x in range(4)]), 0)
            tex = max(sum([ingr[x][3] * recipe[x] for x in range(4)]), 0)
            best = max(best, cap * dur * flav * tex)

print best
