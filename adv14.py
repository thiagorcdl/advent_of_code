#!/usr/bin/python
import sys

f = open('./input14.txt', 'r')
finish = 2503

total = 0
while True:
    line = f.readline().rstrip()
    if not line:
        break
    args = line.split(' ')
    name, speed, traveltime, resttime = args[0], int(args[3]), int(args[6]), int(args[-2])
    time_sum = traveltime + resttime
    total = max(total,  finish / time_sum * speed * traveltime + min(finish % time_sum, traveltime) * speed)
print total