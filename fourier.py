# -*- coding: utf-8 -*- 

""" УСЛОВИЕ ЗАДАЧИ:
    Найти первые count коэффициентов Фурье для заданной функции по тригонометрическому базису. """

import scipy.integrate as integrate
from math import pi, sqrt, sin, exp


# Множитель для аргумента тригонометрических функций базиса
def trigon_mult(k, l, x):
    return (2 * pi * k / l) * x


# Функция, возвращающая k-член системы тригонометрического базиса
def f_base(x, k):
    return sqrt(2 / pi) * sin(k * x)


# Функция для нахождения первого элемента тригонометрического базиса
def f_first(x):
    return sqrt(2 / pi) * sin(x)


# Функция для нахождения определенного интеграла заданной функции по заданным пределам интегрирования
def integral(f, a, b):
    return integrate.quad(f, a, b)[0]


# Функция для нахождения коэффициентов Фурье
def fourier(f, count, a, b):
    return [integral(lambda x: f(x) * f_base(x, i), a, b) for i in range(1, count + 1)]


if __name__ == '__main__':
    print(fourier(lambda x: -5 * exp(-13 * x) * (x - 8) ** 2, 7, 0, 1))
