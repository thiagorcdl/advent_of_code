#!/usr/bin/python2
import sys

f = open('./input7.txt', 'r')
var = {}


def AND(a, b):
    return val(a) & val(b)


def OR(a, b):
    return val(a) | val(b)


def LSHIFT(a, n):
    return val(a) * (2 ** int(n))


def RSHIFT(a, n):
    return val(a) / (2 ** int(n))


def val(key):
    try:
        return int(key)
    except:
        args = var[key]
        if isinstance(args, type(1)):
            return args
        elif len(args) == 1:  # 4000 -> a
            var[key] = 0x0000ffff & val(args[0])
        elif len(args) == 2:  # NOT a -> b
            var[key] = 0x0000ffff & ~ val(args[1])
        else:  # a OP n -> c
            var[key] = 0x0000ffff & eval("%s(args[0],args[2])" % args[1])
    return var[key]


while True:
    line = f.readline().rstrip()
    if not line:
        break
    args = line.split(' ')
    var[args[-1]] = args[:-2]

if len(sys.argv) > 1 and sys.argv[1] == '2':
    # backs up the variables dict; runs part 1; restores dict pointer and assign answer to b
    var2 = var.copy()
    val_a = val('a')
    var = var2
    var['b'] = val_a
print 0x0000ffff & val('a')
