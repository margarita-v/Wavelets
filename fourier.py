# -*- coding: utf-8 -*- 

''' УСЛОВИЕ ЗАДАЧИ:
    Найти первые count коэффициентов Фурье для заданной функции по тригонометрическому базису. '''

import scipy.integrate as integrate
from math import pi, sqrt, sin, cos

# Множитель для аргумента тригонометрических функций базиса
def trigon_mult(k, l, x):
    return (2*pi*k / l)*x

# Функция, возвращающая k-член системы тригонометрического базиса
def f_base(x, l, k, sin_mult, cos_mult):
    return sqrt(2 / l) * ( sin(trigon_mult(k, l, x)) * sin_mult + cos(trigon_mult(k, l, x)) * cos_mult )

# Функция для нахождения первого элемента тригонометрического базиса
def f_first(l):
    return sqrt(1 / l)

# Функция для нахождения определенного интеграла заданной функции по заданным пределам интегрирования
def integral(f, a, b):
    return integrate.quad(f, a, b)[0]

# Функция для нахождения коэффициентов Фурье
def fourier(f, count, l, a, b):
    result = [integral(lambda x: f_first(l) * f(x), a, b)]
    j = 1
    for i in range(1, count):
        if i % 2 == 0:
            result.append(integral(lambda x: f(x) * f_base(x, l, j, 0, 1), a, b))
            j += 1
        else:
            result.append(integral(lambda x: f(x) * f_base(x, l, j, 1, 0), a, b))
    return result

if __name__ == '__main__':
    print(fourier(lambda x: x*x - 5*x, 5, 2*pi, 0, 2*pi))
