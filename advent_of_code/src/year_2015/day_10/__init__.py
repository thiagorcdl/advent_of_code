#!/usr/bin/python2
import sys

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input10.txt', 'r')
input_sequence = f.readline().rstrip()


def look(sequence):
    i = 0
    say = ''
    char = 0
    for i, c in enumerate(sequence):
        if c != sequence[char]:
            say += str(i - char) + sequence[char]
            char = i
    say += str(i - char + 1) + sequence[char]
    return say

for n in range(50 if part2 else 40):
    input_sequence = look(input_sequence)
print len(input_sequence)
