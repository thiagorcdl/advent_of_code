#!/usr/bin/python
import sys
import re

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input8.txt', 'r')
n_code = 0
n_encoded = 0
n_decoded = 0
while True:
    line = f.readline().rstrip()
    if not line:
        print (n_encoded - n_code) if part2 else (n_code - n_decoded)
        break
    n_code += len(line)

    if part2:
        encoded = '"' + line.replace('\\', '\\\\').replace(r'"', r'\"') + '"'
        n_encoded += len(encoded)
    else:
        decoded = re.sub(r'\\x[0-9A-Fa-f][0-9A-Fa-f]|\\"|\\\\', '-', line)[1:-1]
        n_decoded += len(decoded)