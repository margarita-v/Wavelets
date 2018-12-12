# -*- coding: utf-8 -*-

import numpy as np

tab = '\t'


# Функция, выполняющая прямое вейвлет-преобразование для одномерного изображения
def direct_wavelet_transformation(image):
    middle, iteration = len(image) // 2, 1
    one_iter = False
    if middle == 1:
        middle += 1
        one_iter = True
    for i in range(middle - 1):
        new_image = []
        count, step = middle // iteration, 0
        if one_iter:
            count = 1
        for j in range(count):
            first, second = image[step], image[step + 1]
            new_image.insert(step // 2, (first + second) / 2)
            new_image.append((first - second) / 2)
            step += 2
        if iteration > 1:
            new_image += image[-iteration * 2:]
        image = new_image
        iteration += 1
    return image


# Функция, выполняющая обратное вейвлет-преобразование для одномерного изображения
def inverse_wavelet_transformation(image):
    new_image = image.copy()
    middle, step = len(image) // 2, 1
    for i in range(middle - 1):
        index = 0
        temp = new_image.copy()
        for j in range(step):
            first, second = new_image[j], new_image[j + step]
            temp[index], temp[index + 1] = first + second, first - second
            index += 2
        step *= 2
        new_image = temp
    return new_image


# Функция, позволяющая скорректировать значения изображения в соответствии с пороговым значением
def adjust_image(image, threshold, use_abs=False):
    comparator = lambda i: abs(i) > threshold if use_abs else i > threshold
    return [i if comparator(i) else 0 for i in image]


def solve(image, threshold, use_abs=False):
    print_image(image, "image")
    direct = direct_wavelet_transformation(image)
    print_image(direct, "direct")
    adjust = adjust_image(direct, threshold, use_abs)
    print_image(adjust, "adjust")
    print_image(inverse_wavelet_transformation(adjust), "inverse")
    print()


def print_image(image, name):
    print(name + tab, "length =", len(image), "[", tab.join([str(i) for i in image]), "]")


# Функция, выполняющая двумерное вейвлет-преобразование Хаара (пирамидальное)
def pyramid_two_dimensional_transformation(matrix):
    # выполнение одной итерации вейвлет-преобразования к каждой строке
    first_step = np.array([direct_wavelet_transformation(row) for row in matrix])
    # выполнение одной итерации вейвлет-преобразования к кажому стоблцу полученной матрицы
    second_step = np.array([direct_wavelet_transformation(row) for row in first_step.transpose()]).transpose()
    # аналогично для левого верхнего квадранта, пока не дойдем до одного элемента
    size, sec = matrix.shape
    half_size = size // 2
    if half_size == 1:
        return second_step
    indices = [[i for i in range(half_size)], [i + size for i in range(half_size)]]
    quadrant = pyramid_two_dimensional_transformation(np.take(second_step, indices))
    print(quadrant)
    return second_step


if __name__ == '__main__':
    solve([419, 411, 419, 399, 434, 384, 410, 404], 5)
    solve([249, 247, 243, 241, 180, 184, 235, 237], 1, True)

    matrix = np.array([[20, 12, 13, 11], [6, 2, 8, 12], [15, 17, 14, 8], [10, 6, 4, 10]])
    print(pyramid_two_dimensional_transformation(matrix))
