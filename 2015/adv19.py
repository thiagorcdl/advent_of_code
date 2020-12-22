#!/usr/bin/python2
import sys
import re

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input19.txt', 'r').read()

mol = re.findall('\n\n(\w+)', f)[0]
outcomes = []

if part2:
    path = []
    transit = {}
    best = 2 ** 32

    def dissolve():
        global mol
        global best
        if mol == 'e':
            print len(path), path
            return len(path)
        if len(path) >= best - 1:
            # After next transition, it will be just as good as current best
            return best
        # print best, path, len(path)
        for key, val in transit.iteritems():
            for match in re.finditer(key, mol):
                mol = mol[:match.start()] + val + mol[match.end():]
                path.append(val)
                best = min(best, dissolve())
                del path[-1]
                mol = mol[:match.start()] + key + mol[match.start() + len(val):]
        return best
    for key, val in re.findall('(\w+) => (\w+)', f):
            transit[val] = key
    print dissolve()
else:
    for key, val in re.findall('(\w+) => (\w+)', f):
        for match in re.finditer(key, mol):
            outcomes.append(mol[:match.start()] + val + mol[match.end():])
    print len(set(outcomes))



