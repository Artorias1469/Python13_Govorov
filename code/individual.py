#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def custom_function(*args):
    if not args:
        return None

    last_positive_index = None
    for i in range(len(args) - 1, -1, -1):
        if args[i] > 0:
            last_positive_index = i
            break

    if last_positive_index is None:
        return None

    result_sum = sum(args[:last_positive_index])

    return result_sum

if __name__ == "__main__":
    print(custom_function(1, 2, 3, 4, 5))
    print(custom_function(-1, -2, -3, 4, 5))
    print(custom_function())
