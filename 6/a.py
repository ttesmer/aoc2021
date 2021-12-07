#!/usr/bin/python
import math
import itertools as it
import numpy as np
from functools import reduce
from operator import mul, add
from collections import Counter, deque, defaultdict
import networkx as nx
import sys
import re

from advent import *


"""
This guy: https://www.youtube.com/watch?v=fHlWM8CIrlI
had the same solution & problem, but was just way faster. (2nd place)
""" 

def solve(o):
    """Part 2."""

    #d = {k: 0 for k in range(9)}
    # THAT'S what `defaultdict` is for..
    d = defaultdict(int)

    fish = ints(o[0])
    for f in fish:
        d[f] += 1

    for day in range(256):
        print(d)

        incr_six = 0
        for k in range(9):
            if k == 0:
                incr_six = d[k]
                d[k] = 0
            else:
                d[k-1] += d[k]
                d[k] = 0

        d[6] += incr_six
        d[8] += incr_six


    print("\033[92mResult #2:", sum(d[k] for k in d))

def solve_p1(o):
    """Part 1."""
   
    fish = ints(o[0])
    for day in range(80):
        new_fish = []

        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1

        fish += new_fish


    print("\033[92mResult #1:", len(fish))

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
