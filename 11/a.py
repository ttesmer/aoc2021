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
    d = defaultdict()
    s = set()
    q = deque()
    print("\033[92mResult #1:", res, "\033[m")


def solve2(o):
    """Part 2."""

    res = 0
    xs = []

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
