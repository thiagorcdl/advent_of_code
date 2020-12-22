#!/usr/bin/python2
import sys
import itertools

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input13.txt', 'r')
NPEOPLE = 9 if part2 else 8
EXCLUDE = 2 ** 31 if part2 else -(2 ** 31)
people = []
graph = [[0 for x in range(NPEOPLE)] for y in range(NPEOPLE)]

# Builds Graph
while True:
    line = f.readline().rstrip()
    if not line:
        break
    split = line.replace('lose ', '-').replace('gain ', '').split(' ')
    a, value, b = split[0], split[2], split[-1][:-1]
    if a not in people:
        people.append(a)
    if b not in people:
        people.append(b)
    graph[people.index(a)][people.index(b)] += int(value)
    graph[people.index(b)][people.index(a)] += int(value)

# Include yourself in part 2
if part2:
    for i in range(NPEOPLE):
        graph[i][NPEOPLE-1] = 0

# Held-Karp algorithm
peopleset = set(range(NPEOPLE))
costs = [{} for x in range(NPEOPLE)]

for k in range(1, NPEOPLE):
    costs[k]['set([0, %d])' % k] = graph[0][k]

for i in range(2, NPEOPLE + 1):
    for subset in sorted(itertools.combinations(peopleset, i), key=lambda tup: tup[0]):
        for k in reversed(subset):
            try:
                costs[k][repr(set(subset))] = max(
                    [costs[j][repr(set(subset).difference({k}))] + graph[j][k] for j in subset if j not in [0, k]]
                )
            except:
                pass
print max([costs[k][repr(peopleset)] + graph[k][0] for k in range(1, NPEOPLE)])
