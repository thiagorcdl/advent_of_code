#!/usr/bin/python2
import sys
import re

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input11.txt', 'r')
str_pwd = f.readline().rstrip()
pwd = map(ord, list(str_pwd))


def incr(ch):
    return 97 + ((ch - 96) % 26)

for i, char in enumerate(str_pwd):
    if char in ['i', 'o', 'l']:
        pwd[i] = incr(pwd[i])
        for j in range(i+1, 8):
            pwd[j] = 97
        str_pwd = "".join(map(chr, pwd))
        break


def find_next(pwd):
    while True:
        for i, char in enumerate(reversed(pwd)):
            j = -(i + 1)
            # Base is 97 ('a'); uses mod 26 for the offset
            pwd[j] = 97 + ((char - 96) % 26)
            if pwd[j] in ['i', 'o', 'l']:
                # Jumps to next acceptable string | fiaa -> fjaa
                pwd[j] = incr(pwd[i])
            if pwd[j] != 97:
                break
        has_seq = False
        for i, char in enumerate(pwd):
            if i == len(pwd) - 2:
                break
            if pwd[i+1] == pwd[i]+1 and pwd[i+2] == pwd[i]+2:
                has_seq = True
        str_pwd = "".join(map(chr, pwd))
        n_pairs = len(set(re.findall(r'(\w)\1', str_pwd)))
        if n_pairs > 1 and has_seq:
            break
    return str_pwd

next_pwd = find_next(pwd)
if len(sys.argv) > 1 and sys.argv[1] == '2':
    next_pwd = find_next(map(ord, list(next_pwd)))
print next_pwd
