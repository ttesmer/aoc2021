#!/usr/bin/python
import re
import sys
import math
import copy
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

    o, folds = o.split("\n\n")
    folds = lmap(lambda x: x.split(" ")[2].split("="), folds.split("\n"))

    o = lmap(ints, o.split("\n"))

    C, R = max([x[0] for x in o])+1, max([x[1] for x in o])+1
    arr = np.zeros(R*C).reshape(R, C)

    for x, y in o:
        arr[y][x] = 1

    res = 0
    for dim, val in folds[:1]:
        arr2 = arr.copy()
        #print(dim, val)
        val = int(val)
        if dim == "y":
            arr2 = arr2[:val]
            arr = arr[val+1:][::-1]
        elif dim == "x":
            arr = arr.T
            arr2 = arr2.T
            arr = arr[:val][::-1].T
            arr2 = arr2[val+1:].T

        ss = ""
        for row in arr2:
            s = ""
            for col in row:
                if col == 1:
                    s+="#"
                else:
                    s+="."
            s+="\n"
            ss+=s
        #print(ss)

        sx = ""
        for row in arr:
            s = ""
            for col in row:
                if col == 1:
                    s+="#"
                else:
                    s+="."
            s+="\n"
            sx+=s
        #print(sx)

    seen = set()
    for y, row  in enumerate(arr):
        for x, col in enumerate(row):
            if col == 1:
                seen.add((x,y))
                res += 1

    for y, row  in enumerate(arr2):
        for x, col in enumerate(row):
            if col == 1 and (x,y) not in seen:
                res += 1

    print("\033[92mResult #1:", res, "\033[m")


def solve(o):
    """Part 2."""
    o, folds = o.split("\n\n")
    folds = lmap(lambda x: x.split(" ")[2].split("="), folds.split("\n"))

    o = lmap(ints, o.split("\n"))

    C, R = max([x[0] for x in o])+1, max([x[1] for x in o])+1
    arr = np.zeros(R*C).reshape(R, C)

    for x, y in o:
        arr[y][x] = 1

    res = 0
    for dim, val in folds:
        arr2 = arr.copy()
        print(dim, val)
        val = int(val)
        if dim == "y":
            arr2 = arr2[:val]
            arr = arr[val+1:][::-1]
        elif dim == "x":
            arr = arr.T
            arr2 = arr2.T
            arr = arr[:val][::-1].T
            arr2 = arr2[val+1:].T

        assert arr.shape == arr2.shape
        print(arr.shape, arr2.shape)

        idxs = [(x,y) for y, row in enumerate(arr2) for x, col in enumerate(arr2)]

        for y, row in enumerate(arr2):
            for x, col in enumerate(row):
                if arr2[y][x] == 1:
                    arr[y][x] = 1

    sx = ""
    for row in arr:
        s = ""
        for col in row:
            if col == 1:
                s+="#"
            else:
                s+="."
        s+="\n"
        sx+=s[::-1]
    print(sx)

    seen = set()
    for y, row  in enumerate(arr):
        for x, col in enumerate(row):
            if col == 1:
                seen.add((x,y))
                res += 1

    for y, row  in enumerate(arr2):
        for x, col in enumerate(row):
            if col == 1 and (x,y) not in seen:
                res += 1

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
        o = open(case, "r").read().strip()#.split("\n")
        solve(o)


if __name__ == "__main__":
    run()
