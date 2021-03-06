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
    return math.exp(-15 * abs(x - 0.3)) + x * x


def get_coeff(f, a, b):
    return integrate.quad(lambda x: base(x) * f(x), a, b)[0]


if __name__ == "__main__":
    print(get_coeff(lambda x: 1, 0, 1))
    for n in range(0, 3):
        for k in range(0, 2 ** n):
            print(get_coeff(lambda x: haar_f(x, n, k), 0, 1))
