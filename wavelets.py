# -*- coding: utf-8 -*-

""" УСЛОВИЕ ЗАДАЧИ:
    Вычислить матрицу вейвлет-коэффициентов [W(psi)f](i, j) для сигнала f(t).

    Использовать в качестве материнского вейвлет psi(t)

    Формула для решения
    [W(psi)f](a, b) = integral(-infinity, +infinity)(f(t) * psi(ab)(t))dt,
    где psi(ab)(t) = |a|^(-1/2) * psi((t - b) / a)
"""

from math import pi, cos, exp

import scipy.integrate as integrate
from numpy import inf, conjugate


# Функция, задающая сигнал
def f(t):
    return cos(pi * t / 4) * t ** 2


# Функция, задающая материнский вейвлет
def psi(t):
    # MHAT-вейвлет
    return (t ** 2 - 1) * exp(-t ** 2 / 2)


def psi_ab(a, b, t):
    return abs(a) ** (-0.5) * psi((t - b) / a)


# Функция, вычисляющая матрицу вейвлет-коэффициентов
def solve(i, j):
    return integral(lambda t: f(t) * conjugate(psi_ab(i, j, t)))


# Функция для нахождения определенного интеграла заданной функции по заданным пределам интегрирования
def integral(f, a=-inf, b=+inf):
    return integrate.quad(f, a, b)[0]


if __name__ == '__main__':
    for i in range(1, 3):
        for j in range(1, 4):
            print(solve(i, j))
        print()
