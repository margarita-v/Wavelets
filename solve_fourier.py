# -*- coding: utf-8 -*- 

""" УСЛОВИЕ ЗАДАЧИ:
    Найти первые count коэффициентов Фурье для заданной функции по тригонометрическому базису. """

import scipy.integrate as integrate
from math import pi, sqrt, sin, cos


# Функция, для которой требуется посчитать коэффициенты Фурье
def f(x):
    return x * x - 5 * x


# Множитель для аргумента тригонометрических функций базиса
def trigon_mult(k, l, x):
    return (2 * pi * k / l) * x


# Функция, возвращающая k-член системы тригонометрического базиса
def f_base(x, l, k, sin_mult, cos_mult):
    return sqrt(2 / l) * (sin(trigon_mult(k, l, x)) * sin_mult + cos(trigon_mult(k, l, x)) * cos_mult)


# Функция для нахождения первого элемента тригонометрического базиса
def f_first(l):
    return sqrt(1 / l)


# Функция для нахождения определенного интеграла заданной функции по заданным пределам интегрирования
def integral(f, a, b):
    return integrate.quad(f, a, b)[0]


if __name__ == '__main__':
    # Параметр для тригонометрического базиса
    l = 2 * pi
    # Количество коэффициентов Фурье, которые требуется найти
    count = 5
    # Параметры поля L^2(a, b)
    a = 0
    b = l
    result = [integral(lambda x: f_first(l) * f(x), a, b)]
    j = 1
    for i in range(1, count):
        if i % 2 == 0:
            result.append(integral(lambda x: f(x) * f_base(x, l, j, 0, 1), a, b))
            j += 1
        else:
            result.append(integral(lambda x: f(x) * f_base(x, l, j, 1, 0), a, b))
    print(result)
