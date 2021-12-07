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

    o = ints(o[0])
    res = 0
    xs = []
    small = math.inf

    for j in range(min(o), max(o)+1):
        res = 0

        for k in o:
            res += abs(k-j)
            
        if res < small:
            small = res

    print("\033[92mResult #1:", small)

def solve(o):
    """Part 2:
    Brute force, horribly slow, but it works.
    """

    o = ints(o[0])
    res = 0
    xs = []
    small = math.inf

    for j in range(min(o), max(o)+1):
        res = 0

        for k in o:
            res += sum([*range(1, abs(k-j)+1)])
        print(j, res)
            
        if res < small:
            small = res

    print("\033[92mResult #2:", small)


def run():
    """Run tests and real input"""
    try:
        args = sys.argv[1]
        for case in args:
            print("\nCase", '"' + case + '":')
            o = open(case, "r").read().strip().split("\n")
            solve(o)
    except IndexError as e:
        print("\033[91mError: No file piped!\033[0m")


if __name__ == "__main__":
    run()
