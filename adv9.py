#!/usr/bin/python
import sys
import copy

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input9.txt', 'r')
NCITIES = 8
EXCLUDE = -1 if part2 else 2 ** 31
cities = []
graph = [[0 for x in range(NCITIES)] for x in range(NCITIES)]

while True:
    line = f.readline().rstrip()
    if not line:
        break
    a, to, b, equals, distance = line.split(' ')
    if a not in cities:
        cities.append(a)
    if b not in cities:
        cities.append(b)
    graph[cities.index(a)][cities.index(b)] = int(distance)
    graph[cities.index(b)][cities.index(a)] = int(distance)


totals = []
for city in cities:
    graph2 = copy.deepcopy(graph)
    c = cities.index(city)
    traversed = []
    visited = [c, ]
    total = 0
    trip = cities[c]
    while len(visited) < NCITIES:
        graph2[visited[-1]][visited[-1]] = EXCLUDE
        if len(visited) > 1:
            graph2[visited[-1]][visited[-2]] = EXCLUDE
        options = graph2[visited[-1]]
        distance = max(*options) if part2 else min(*options)
        peer = options.index(distance)
        while peer in visited:
            start = peer + 1
            peer = options.index(distance, start)
        total += distance
        graph2[visited[-1]] = [EXCLUDE for i in range(NCITIES)]
        for i in range(NCITIES):
            graph2[i][visited[-1]] = EXCLUDE
        visited.append(peer)
    totals.append(total)

print max(totals) if part2 else min(totals)
