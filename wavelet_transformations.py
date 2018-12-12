# -*- coding: utf-8 -*-

tab = '\t'


# Функция, выполняющая прямое вейвлет-преобразование для одномерного изображения
def direct_wavelet_transformation(image):
    middle, iteration = len(image) // 2, 1
    for i in range(middle - 1):
        new_image = []
        count, step = middle // iteration, 0
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


if __name__ == '__main__':
    solve([419, 411, 419, 399, 434, 384, 410, 404], 5)
    solve([249, 247, 243, 241, 180, 184, 235, 237], 1, True)
