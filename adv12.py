#!/usr/bin/python
import re

f = open('./input12.txt', 'r')
injson = f.readline().rstrip()
nums = map(int, re.findall(r'\-?\d+', injson))

print sum(nums)
