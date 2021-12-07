#!/usr/bin/python
import math
import itertools as it
import numpy as np
import re

def solve(o):
    """Part 2."""

    play = o[0].split(",")
    bs = [[x.strip().split(" ") for x in re.sub(' +', ' ', b).split("\n")] for b in o[1:]]
    tr = lambda xxx: list(map(list, zip(*xxx)))
    fin = 0
    new_bs = bs
    res = 0
    lst = []
    cpy_bs = new_bs
    for p in play:
        cpy_bs = new_bs
        for i, b in enumerate(new_bs):
            for r in b:
                if all([n == "X" for n in r]):
                    del cpy_bs[i]
            for c in tr(b):
                if all([n == "X" for n in c]):
                    del cpy_bs[i]
        new_bs = cpy_bs
        print(p)
        for bi, b in enumerate(new_bs):
            for row in b:
                print(row)
            print()
            for ri, r in enumerate(b):
                for i,n in enumerate(r):
                    if n == p:
                        cpy_bs[bi][ri][i] = "X"
                if r.count("X") == len(r):
                    summ = 0
                    for r in cpy_bs[bi]:
                        for n in r:
                            if n != "X":
                                summ += int(n)
                    lst.append(int(p)*summ)
                    print(summ, int(p), "\nResult:", summ*int(p))
                    if len(new_bs) == 1:
                        res = True
                        break
            if res: break
            for ci, c in enumerate(tr(b)):
                if c.count("X") == len(c):
                    summ = 0
                    for c in tr(cpy_bs[bi]):
                        for n in c:
                            if n != "X":
                                summ += int(n)
                    lst.append(int(p)*summ)
                    print(summ, int(p), "\nResult:", summ*int(p))
                    if len(new_bs) == 1:
                        res = True
                        break
            if res: break
        if res: break

def solve_1(o):
    """Part 1."""

    play = o[0].split(",")
    bs = [[x.split(" ") for x in re.sub(' +', ' ', b).split("\n")] for b in o[1:]]
    tr = lambda xxx: list(map(list, zip(*xxx)))
    fin = 0
    new_bs = bs
    res = 0
    for p in play:
        if res: break
        for bi, b in enumerate(new_bs):
            for ci, c in enumerate(tr(b)):
                if c.count("X") == len(c):
                    summ = 0
                    for c in new_bs[bi]:
                        print(c)
                        for n in c:
                            if n != "X":
                                summ += int(n)
                    print(int(p)*summ)
                    res = True
                    break
                if res: break
            for ri, r in enumerate(b):
                for i,n in enumerate(r):
                    if n == p:
                        new_bs[bi][ri][i] = "X"
                if r.count("X") == len(r):
                    summ = 0
                    for r in new_bs[bi]:
                        print(r)
                        for n in r:
                            if n != "X":
                                summ += int(n)
                    print(int(p)*summ)
                    res = True
                    break
                if res: break
            if res: break

def run():
    """Run tests and real input"""
    for case in "ti":
        print("\nresult for case", case, ":")
        o = open(case, "r").read().strip().split("\n\n")
        solve(o)


if __name__ == "__main__":
    run()
