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

def solve1(o):
    """Part 1."""

    o = lmap(lambda x: lmap(int,re.findall("[0-9]", x)), o)
    res = 0
    d = defaultdict(int)
    for i,j in enumerate(o):
        if i == 0:
            for ni, n in enumerate(j):
                # check adjacent numbers
                if ni != 0 and ni != len(j)-1:
                    if j[ni-1] > n and j[ni+1] > n and o[i+1][ni] > n:
                        d[n] += 1
                elif ni == 0:
                    if j[ni+1] > n and o[i+1][ni] > n:
                        d[n] += 1
                elif ni == len(j)-1:
                    if j[ni-1] > n and o[i+1][ni] > n:
                        d[n] += 1

        elif i == len(o)-1:
            for ni, n in enumerate(j):
                # check adjacent numbers
                if ni != 0 and ni != len(j)-1:
                    if j[ni-1] > n and j[ni+1] > n and o[i-1][ni] > n:
                        d[n] += 1
                elif ni == 0:
                    if j[ni+1] > n and o[i-1][ni] > n:
                        d[n] += 1
                elif ni == len(j)-1:
                    if j[ni-1] > n and o[i-1][ni] > n:
                        d[n] += 1
        else:
            for ni, n in enumerate(j):
                # check adjacent numbers
                if ni != 0 and ni != len(j)-1:
                    if j[ni-1] > n and j[ni+1] > n and o[i-1][ni] > n and o[i+1][ni] > n:
                        d[n] += 1
                elif ni == 0:
                    if j[ni+1] > n and o[i-1][ni] > n and o[i+1][ni] > n:
                        d[n] += 1
                elif ni == len(j)-1:
                    if j[ni-1] > n and o[i-1][ni] > n and o[i+1][ni] > n:
                        d[n] += 1

    for k, v in d.items():
        res += v*(k+1)
    print("\033[92mResult #1:", res)

def solve(o):
    """Part 2."""

    o = lmap(lambda x: lmap(int,re.findall("[0-9]", x)), o)
    res = 0
    dr = [-1,0,1,0]
    dc = dr[::-1]
    visited = set()
    xs = []

    # iterate over indices of low points
    # and perform BFS for flood fill
    # then return size of basins multiplied
    for r in range(len(o)):
        for c in range(len(o[0])):
            if (r,c) not in visited and o[r][c] != 9:
                size = 0
                q = deque()
                q.append((r,c))
                while q:
                    (r,c) = q.pop()
                    if (r,c) in visited:
                        continue
                    visited.add((r,c))
                    size += 1
                    for d in range(4):
                        rp = r+dr[d]
                        cp = c+dc[d]
                        if 0 <= rp < len(o) and 0 <= cp < len(o[0]) and o[rp][cp] != 9:
                            q.append((rp,cp))
                xs.append(size)
    xs.sort()
    res = reduce(mul, xs[-1:-4:-1])
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
