#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_mean(*args):
    if not args:
        return None

    if any(arg == 0 for arg in args):
        return None

    reciprocal_sum = sum(1 / float(arg) for arg in args)
    harmonic_mean = len(args) / reciprocal_sum
    return harmonic_mean

def main():
    data1 = (2, 4, 8)
    data2 = (1, 0, 3)
    data3 = ()

    result1 = harmonic_mean(*data1)
    result2 = harmonic_mean(*data2)
    result3 = harmonic_mean(*data3)

    print(f"Среднее гармоническое для {data1}: {result1}")
    print(f"Среднее гармоническое для {data2}: {result2}")
    print(f"Среднее гармоническое для {data3}: {result3}")

if __name__ == "__main__":
    main()
