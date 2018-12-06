# -*- coding: utf-8 -*-

import scipy.integrate as integrate
import math


# Базисная функция - вейвлет Хаара
def psi(x):
    if 0 <= x < .5:
        return 1
    if .5 <= x < 1:
        return -1
    return 0


# Функция, задающая систему вейвлетов Хаара
def haar_f(x, n, k):
    return (2 ** (n * .5)) * psi((2 ** n) * x - k)


# Функция, для которой необходимо вычислить коэффициенты Фурье по системе Хаара
def base(x):
    return 20 * (math.sin(4 * x) ** 2) - math.sin(15 * x)


def get_coeff(f, a, b):
    return integrate.quad(lambda x: base(x) * f(x), a, b)[0]


if __name__ == "__main__":
    n = 2
    for k in range(0, 2 ** n):
        print(get_coeff(lambda x: haar_f(x, 2, k), 0, 1))
