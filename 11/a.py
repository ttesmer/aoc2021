#!/usr/bin/python
import re
import sys
import math
import numpy as np
import networkx as nx
import itertools as it
from functools import reduce
from operator import mul, add
from statistics import median
from collections import Counter, deque, defaultdict

from advent import *

def solve1(o):
    """Part 1."""

    o = [[int(x) for x in row] for row in o]
    res = 0

    flashes = 0
    for step in range(100):
        # incr all elements by 1
        o = [[x+1 for x in row] for row in o]

        # get indices for elements > 9
        stack = [(r,c) for r, j in enumerate(o) for c, j2 in enumerate(j) if j2 > 9]

        # DFS
        while stack:
            (r, c) = stack.pop()
            flashes += 1
            for (dr, dc) in neighbors((r,c), o):
                o[dr][dc] += 1
                if o[dr][dc] == 10:
                    stack.append((dr,dc))
        o = [[0 if n > 9 else n for n in row] for row in o]

    res = flashes
    print("\033[92mResult #1:", res, "\033[m")


def solve(o):
    """Part 2."""

    o = [[int(x) for x in row] for row in o]
    res = 0
    step = 0
    while True:
        step += 1
        flashes = 0
        # incr all elements by 1
        o = [[x+1 for x in row] for row in o]

        # get indices for elements > 9
        stack = [(r,c) for r, j in enumerate(o) for c, j2 in enumerate(j) if j2 > 9]

        # DFS
        while stack:
            (r, c) = stack.pop()
            flashes += 1
            for (dr, dc) in neighbors((r,c), o):
                o[dr][dc] += 1
                if o[dr][dc] == 10:
                    stack.append((dr,dc))
        res += flashes
        if flashes == 100:
            res = step
            break
        o = [[0 if n > 9 else n for n in row] for row in o]

    print("\033[92mResult #2:", res, "\033[m")


def run():
    """Run tests and real input"""
    try:
        args = sys.argv[1]
    except:
        print("\033[91mErpor: No file piped!\033[0m")
        exit()
    for case in args:
        print("\nCase", '"' + case + '":')
        o = open(case, "r").read().strip().split("\n")
        solve(o)



if __name__ == "__main__":
    run()
