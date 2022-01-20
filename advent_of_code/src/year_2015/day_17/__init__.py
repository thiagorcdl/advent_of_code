#!/usr/bin/python2
import sys
import re

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input17.txt', 'r').read()
eggnog = 150
refr = map(int, re.findall('(\d+)', f))
size = len(refr)
answers = []


def search(last_sum, start, answer):
    for i in range(start, size):
        cur_sum = last_sum + refr[i]
        cur_answer = answer + [refr[i],]
        if cur_sum < eggnog:
            search(cur_sum, i+1, cur_answer)
        elif cur_sum == eggnog:
            answers.append(cur_answer)

search(0, 0, [])
lengths = map(len, answers)
print lengths.count(min(lengths)) if part2 else len(answers)