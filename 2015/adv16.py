#!/usr/bin/python2
import re
import sys

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input16.txt', 'r')

aunt = []
truth = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}
naunt = 1
matches = 0
aunt = 0

while True:
    line = f.readline().rstrip()
    if not line:
        break
    clues = {}

    for x in re.split(r'\d+: ', line)[1].split(','):
        key, val = x.split(":")
        key = key.lstrip().rstrip()
        val = int(val)
        if part2 and ((key in ['cats', 'trees'] and val <= truth[key]) or
           (key in ['pomeranians', 'goldfish'] and val >= truth[key]) or
           (truth[key] != val)) or truth[key] != val:
            continue
        clues[key] = val
    aunt, matches = (naunt, len(clues)) if len(clues) > matches else (aunt, matches)
    naunt += 1
print aunt
