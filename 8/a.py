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

def solve2(o):
    """Part 2."""

    res = 0

    print("\033[92mResult #2:", res)

def solve(o):
    """Part 1."""

    d = defaultdict()
    res = 0
    xs = []
    small = math.inf
    s = ""

    print("\033[92mResult #1:", small)


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
