import math
import numpy as np
import re
import json

def run():
    o = [*map(int, open("i", "r").read().strip().split("\n"))]
    #o = [*map(int, open("tests", "r").read().strip().split("\n"))]
    acc = 0
    c = []
    s = {}
    p = ""
    w = [sum(w) for w in zip(o, o[1:], o[2:])]
    print(sum(b > a for a, b in zip(w, w[1:])))

run()
