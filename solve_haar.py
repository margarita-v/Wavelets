# -*- coding: utf-8 -*-

from scipy.integrate import quad
import math


def test(x):
    return 20 * (math.sin(4 * x) ** 2) - math.sin(15 * x)


def getStart(i, dev):
    return (i - 1) / dev


def getMiddle(i, dev):
    return (i - 1.0) / dev + 1.0 / (dev * 2.0)


def getEnd(i, dev):
    return i / dev


def integral(x, n):
    return test(x) * 2 ** (n / 2)


n = 2
i = 1
dev = 2 ** n

for i in range(1, dev + 1):
    print(n, i)
    ans1, err1 = quad(integral, getStart(i, dev), getMiddle(i, dev), n)
    ans2, err2 = quad(integral, getMiddle(i, dev), getEnd(i, dev), n)
    print(ans1 - ans2)
