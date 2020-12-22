#!/usr/bin/python2
import sys
import re
import json

f = open('./input12.txt', 'r')
injson = f.readline().rstrip()


def search(current):
    items = []
    if isinstance(current, dict):
        items = current.iteritems()
    elif isinstance(current, list):
        items = enumerate(current)
    for key, item in items:
        if isinstance(item, dict):
            current[key] = 0 if "red" in item.itervalues() else search(item)
        elif isinstance(item, list):
            current[key] = search(item)
    return current

if len(sys.argv) > 1 and sys.argv[1] == '2':
    ldjson = json.loads(injson)
    ldjson = search(ldjson)
    injson = json.dumps(ldjson)

print sum(map(int, re.findall(r'\-?\d+', injson)))
