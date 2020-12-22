#!/usr/bin/python2
import sys

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input3.txt', 'r')
instructions = f.readline().rstrip()

directions = {
    '^': (0, 1), 
    '>': (1, 0), 
    'v': (0, -1), 
    '<': (-1, 0)
}

turn = 0
visited = [(0, 0), ]
current = [(0, 0), (0, 0)]

for char in instructions:
    current[turn] = tuple(map(sum, zip(current[turn], directions[char])))
    visited.append(current[turn])
    if part2:
        turn ^= 1

print len(list(set(visited)))
