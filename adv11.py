#!/usr/bin/python
import sys
import re

part2 = len(sys.argv) > 1 and sys.argv[1] == '2'
f = open('./input11.txt', 'r')
str_pwd = f.readline().rstrip()
pwd = map(ord, list(str_pwd))


while True:
    for i, char in enumerate(reversed(pwd)):
        j = -(i + 1)
        # Base is 97 ('a'); uses mod 26 for the offset
        pwd[j] = 97 + ((char - 96) % 26)
        if pwd[j] in ['i', 'o', 'l']:
            # Jumps to next acceptable string | fiaa -> fjaa
            pwd[j] = 97 + ((char - 96) % 26)
        if pwd[j] != 97:
            break
    has_seq = False
    for i, char in enumerate(pwd):
        if i == len(pwd) - 2:
            break
        if pwd[i+1] == pwd[i]+1 and pwd[i+2] == pwd[i]+2:
            has_seq = True
    str_pwd = "".join(map(chr, pwd))
    n_pairs = len(set(re.findall(r'(\w)\1{1}', str_pwd)))
    if n_pairs > 1 and  has_seq :
        break
    # print str_pwd

print str_pwd