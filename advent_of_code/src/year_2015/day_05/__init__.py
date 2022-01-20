#!/usr/bin/python2
import sys

f = open('./input5.txt', 'r')
total = 0
while True:
    line = f.readline().rstrip()
    if not line:
        print total
        break
    tem_par, tem_amigo = False, False
    for i in range(len(line)-2):
        par = line[i:i+2]
        resto = line[i+2:]
        if par[0] == resto[0]:
            tem_amigo = True
        if len(resto) > 1:
            for j in range(len(resto)):
                par2 = resto[j:j+2]
                if par == par2:
                    tem_par = True
                    break
        if tem_par and tem_amigo:
            total += 1
            break
