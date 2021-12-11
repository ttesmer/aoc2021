import math
import typing
import re
import networkx as nx
import collections
import itertools
import numpy as np
from functools import reduce
from operator import add, mul
import sys


"""
1. Copy this file to python path:
    $ cp advent.py "`python -m site --user-site`"
2. Import wherever you need it:
    from advent import *
"""

"""
String Operations
"""

def ints(s: str) -> typing.List[int]:
    """Return ints in a string"""
    return lmap(int, re.findall(r"-?\d+", s))


def floats(s: str) -> typing.List[float]:
    """Return ints in a string"""
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)

"""
List Operations
"""

def lmap(func, *iterables):
    return list(map(func, *iterables))


def even_indices(xs: list) -> list:
    """Return list of elements with even indices"""
    return xs[slice(1, len(xs), 2)]


def odd_indices(xs: list) -> list:
    """Return list of elements with odd indices"""
    return xs[slice(0, len(xs), 2)]


def product(xs: list) -> list:
    return reduce(mul, xs)


"""
Grid Algorithms/Operations
"""

def neighbors(rc: tuple, m: typing.List[list],  diag=True, elem=False) -> typing.List[tuple]:
    """Return indices or elements of neighbors in grid."""
    r, c = rc
    R, C = len(m), len(m[0])
    neighbor_indices = []

    if -1 < r < R and -1 < c < C:
        if diag:
            for dr in range(r-1, r+2):
                for dc in range(c-1, c+2):
                    if (0 <= dr < R) and (r != dr or c != dc) and (0 <= dc < C):
                        neighbor_indices.append((dr, dc))
        else:
            for dr in range(r-1, r+2):
                for dc in range(c-1, c+2):
                    if (0 <= dr < R) and (r == dr and c != dc) and (0 <= dc < C):
                        neighbor_indices.append((dr, dc))
                    elif (0 <= dr < R) and (r != dr and c == dc) and (0 <= dc < C):
                        neighbor_indices.append((dr, dc))
    else:
        raise Exception("(neighbors) index must be within grid size")

    if not elem:
        return neighbor_indices
    else:
        return [m[dx][dy] for dx, dy in neighbor_indices]


def tr(xs: list) -> list:
    """Transpose a list of lists:
        >>> tr([[1,2],[3,4]])
        [[1,3],[2,4]]
    """
    return lmap(list, zip(*xs))


if __name__ == "__main__":
    # TODO: Implement tests
    pass
