#!/usr/bin/python
import sys

part2 = True or len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input14.txt', 'r')
finish = 2504

total = 0
timeline = [[] for s in range(finish)]
stars = []


def distance(speed, traveltime, resttime, finish=finish):
    time_sum = traveltime + resttime
    return finish / time_sum * speed * traveltime + min(finish % time_sum, traveltime) * speed

while True:
    line = f.readline().rstrip()
    if not line:
        break
    args = line.split(' ')
    name, speed, traveltime, resttime = args[0], int(args[3]), int(args[6]), int(args[-2])
    if part2:
        for t in range(1, finish + 1):
            timeline[t-1].append(distance(speed, traveltime, resttime, t))
        stars.append(0)
    else:
        total = max(total,  distance(speed, traveltime, resttime))

if part2:
    for t in range(finish):
        print t+1, timeline[t], max(timeline[t])
        stars[timeline[t].index(max(timeline[t]))] += 1
    print stars
    print max(stars)
else:
    print total
