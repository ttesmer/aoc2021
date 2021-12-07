#!/usr/bin/python
import math
import itertools as it
import numpy as np
from functools import reduce
from operator import mul, add
from collections import Counter, deque, defaultdict
import re

from advent import *

def solve(o):
    """Part 2."""
   
    res = 0
    lst = []

    coords = []
    for j in o:
        cord = lmap(ints, j.split(" -> "))
        coords.append(cord)

    seen = []
    for (x1, y1), (x2, y2) in coords:
            if y1 == y2 :
                covers = list(zip(range(min(x1,x2), max(x1,x2)+1), [y1 for _ in range((max(x1,x2) - min(x1,x2))+1)]))
            elif x2 == x1:
                covers = list(zip([x1 for _ in range((max(y1,y2) - min(y1,y2))+1)], range(min(y1,y2), max(y1,y2)+1)))
            elif y1 == x2:
                covers = list(zip(reverse([*range(min(x1,x2), max(x1,x2)+1)]), range(min(y1,y2), max(y1, y2)+1)))
            elif y2 == x1:
                covers = list(zip(([*range(min(x1,x2), max(x1,x2)+1)]), range(min(y1,y2), max(y1, y2)+1)))
            else:
                if y1 > y2 and x1 > x2:
                    covers = list(zip(reverse(range(x2,x1+1)), reverse(range(y2,y1+1))))
                elif y1 > y2:
                    covers = list(zip(range(x1,x2+1), reverse(range(y2,y1+1))))
                elif x1 > x2:
                    covers = list(zip(reverse(range(x2,x1+1)), range(y1, y2+1)))
                else:
                    covers = list(zip(range(min(x1,x2), max(x1,x2)+1), range(min(y1,y2), max(y1, y2)+1)))

            #print(covers, (x1,y1), "->", (x2, y2))
            for x, y in covers:
                seen.append((x, y))

    res = Counter(seen)
    a = 0
    for key in res:
        if res[key] >= 2:
            a += 1
    print(a)


def run():
    """Run tests and real input"""
    for case in "ti":
        print("\nCase", '"' + case + '":')
        o = open(case, "r").read().strip().split("\n")
        solve(o)


if __name__ == "__main__":
    run()
