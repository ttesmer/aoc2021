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

def solve(o):
    """Part 1."""

    res = 0
    xs = []

    d = {"(": 1, "[": 2, "{": 3, "<": 4}
    matches = ["()", "[]", "{}", "<>"]
    closed = ">])}"
    for j in o:
        while True:
            for m in matches:
                j = j.replace(f"{m}", "")

            if all([x not in j for x in matches]): 
                break

        if not all([x not in j for x in closed]):
            continue
        else:
            xs.append(j)

    ys = []
    for j in xs:
        score = 0
        for p in j[::-1]:
            score *= 5
            score += d[p]
        ys.append(score)
        print("not corrupted:", j)

    print(ys)
    res = median(ys)
    print("\033[92mResult #2:", res, "\033[m")

def solve1(o):
    """Part 1."""

    res = 0
    xs = []

    d = {")": 3, "]": 57, "}": 1197, ">": 25137}
    matches = ["()", "[]", "{}", "<>"]
    closed = ">])}"
    for j in o:

        while True:
            for m in matches:
                j = j.replace(f"{m}", "")

            if all([x not in j for x in matches]): 
                break

        if all([x not in j for x in closed]):
            continue

        #print("corrupted:",j)
        for pi, p in enumerate(j[1:]):
            if p in closed:
                res += d[p]
                break

    print("\033[92mResult #1:", res, "\033[m")


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
