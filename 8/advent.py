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


def lmap(func, *iterables):
    return list(map(func, *iterables))


def tr(xs: list) -> list:
    """Transpose a list of lists:
        >>> tr([[1,2],[3,4]])
        [[1,3],[2,4]]
    """
    return lmap(list, zip(*xs))


def ints(s: str) -> typing.List[int]:
    """Return ints in a string"""
    return lmap(int, re.findall(r"-?\d+", s))


def floats(s: str) -> typing.List[float]:
    """Return ints in a string"""
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)


def even_indices(xs: list) -> list:
    """Return list of elements with even indices"""
    return xs[slice(1, len(xs), 2)]


def odd_indices(xs: list) -> list:
    """Return list of elements with odd indices"""
    return xs[slice(0, len(xs), 2)]


def reverse(xs: list) -> list:
    return xs[::-1]


def product(xs: list) -> list:
    return reduce(mul, xs)


if __name__ == "__main__":
    # TODO: implement tests
    pass
