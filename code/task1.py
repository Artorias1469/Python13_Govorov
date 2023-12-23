#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pow


def geometric_mean(*args):
    if not args:
        print("Необходимо передать хотя бы один аргумент.")
        return None

    numbers = [float(arg) for arg in args]
    value = 1

    for num in numbers:
        value *= num

    result = pow(value, 1 / len(numbers))
    return result


def main():
    numbers1 = [2, 4, 8]
    result1 = geometric_mean(*numbers1)
    print(f"Среднее геометрическое для {numbers1}: {result1}")

    numbers2 = [1, 3, 5, 7]
    result2 = geometric_mean(*numbers2)
    print(f"Среднее геометрическое для {numbers2}: {result2}")

    result3 = geometric_mean()
    print(f"Среднее геометрическое для пустого списка: {result3}")


if __name__ == "__main__":
    main()
