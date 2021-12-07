#!/usr/bin/python
import math
import itertools as it
import numpy as np
import re
import sys

def solve_p1(o):
    """Part 1."""

    acc = 0
    c = []
    s = ""
    arr = np.array([r for r in o]).reshape(len(o),1).T
    b = False

    gamma = ""
    eps = ""
    tr = [""]
    for i in range(len(o[0])):
        c.append([r[i] for r in o])

    for i in c:
        if i.count("0") > i.count("1"):
            gamma += "0"
        else:
            gamma += "1"

        if i.count("0") > i.count("1"):
            eps += "1"
        else:
            eps += "0"

        
    g = int(gamma, 2)
    e = int(eps, 2)
    print(g*e)

def solve(o):
    """Part 2."""

    acc = 0
    c = []
    s = ""
    b = False

    co2 = ""
    oxy = ""
    c = [[r[x] for r in o] for x in range(len(o[0]))]

    cpy_o = o
    for j in range(len(c)):
        i = [[r[x] for r in cpy_o] for x in range(len(o[0]))][j]
        print(i)
        if i.count("0") > i.count("1"):
            cpy_o = [r for r in cpy_o if r[j] == "0"]
        elif i.count("1") > i.count("0"):
            cpy_o  = [r for r in cpy_o if r[j] == "1"]
        elif i.count("1") == i.count("0"):
            cpy_o = [r for r in cpy_o if r[j] == "1"]
        if len(cpy_o) == 1:
            oxy = cpy_o[0]
            print(oxy)
            break

    cpy_o = o
    for j in range(len(c)):
        i = [[r[x] for r in cpy_o] for x in range(len(o[0]))][j]
        print(i)
        if i.count("0") > i.count("1"):
            cpy_o = [r for r in cpy_o if r[j] == "1"]
        elif i.count("1") > i.count("0"):
            cpy_o  = [r for r in cpy_o if r[j] == "0"]
        elif i.count("1") == i.count("0"):
            cpy_o = [r for r in cpy_o if r[j] == "0"]
        if len(cpy_o) == 1:
            co2 = cpy_o[0]
            print(oxy)
            break

    c = int(co2, 2)
    o = int(oxy, 2)
    print(c*o)



def run(args):
    """Run tests and real input"""
    for case in ["i", "t"]:
        print("\nresult for case", case, ":")
        o = open(case, "r").read().strip().split("\n")
        solve(o)


if __name__ == "__main__":
    run(sys.argv[1:])
