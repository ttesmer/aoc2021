#!/usr/bin/python
import re
import sys
import math
import numpy as np
import networkx as nx
import itertools as it
from functools import reduce
from operator import mul, add
from collections import Counter, deque, defaultdict

from advent import *

def solve(o):
    """Part 2."""

    *o, = map(lambda x: lmap(words, x.split(" | ")), o)
    res = 0
    d = {}
    dc = {}

    for j in o:
        *k, = map(lambda x: reduce(add, sorted(x)), j[0])

        for i in k:
            if len(i) == 2:
                d[i] = 1
                dc[1] = i
            elif len(i) == 4:
                d[i] = 4
                dc[4] = i
            elif len(i) == 3:
                d[i] = 7
                dc[7] = i
            elif len(i) == 7:
                d[i] = 8
                dc[8] = i

        for i in k:
            # 9, 0 or 6?
            if len(i) == 6:
                if all([x in i for x in dc[1]]) :
                    # 9 or 0?
                    if len([x for x in dc[4] if x in i]) == 4:
                        d[i] = 9
                    elif len([x for x in dc[4] if x in i]) == 3:
                        d[i] = 0
                else:
                    d[i] = 6

            # 3, 5 or 2?
            elif len(i) == 5:
                if all([xx in i for xx in dc[7]]):
                    d[i] = 3
                else:
                    # 2 or 5?
                    if len([x for x in dc[4] if x in i]) == 3:
                        d[i] = 5
                    else:
                        d[i] = 2


        st = ""
        for p in j[1]:
            p = reduce(add, sorted(p))
            st += str(d[p])
        #print(st)
        res += int(st)
                
    print("\033[92mResult #2:", res)

def solve1(o):
    """Part 1."""

    *o, = map(lambda x: lmap(words, x.split(" | ")), o)
    res = 0
    for j in o:
        for i in j[1]:
            if len(i) not in [5,6]:
                res += 1

    print("\033[92mResult #1:", res)


def run():
    """Run tests and real input"""
    try:
        args = sys.argv[1]
    except IndexError as e:
        print("\033[91mError: No file piped!\033[0m")
    for case in args:
        print("\nCase", '"' + case + '":')
        o = open(case, "r").read().strip().split("\n")
        solve(o)


if __name__ == "__main__":
    run()
