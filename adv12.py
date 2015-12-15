#!/usr/bin/python
import sys
import re

f = open('./input12.txt', 'r')
injson = f.readline().rstrip()

if True or len(sys.argv) > 1 and sys.argv[1] == '2':
    injson = re.sub('("\w+":\{("\w+":("\w+"|\-?\d+|\[.*\]|\{.*\}),)*"\w+":"red"(,"\w+":("\w+"|\-?\d+|\[.*\]|\{.*\}))*\})', '', injson)
print sum(map(int, re.findall(r'\-?\d+', injson)))
