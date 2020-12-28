"""
Prog:   Lab2.py
Auth:   Oleksii Krutko, IO-z91
Desc:   Theory of probability Lab 2. 2020
"""

import random
import math


def theoretical_standard_deviation():
    print("Theoretical standard deviation for even distribution:")
    print(0.0)


def theoretical_expected_value(a, b):
    print("Theoretical expected value for even distribution between {0} and {1}:", a, b)
    print((a + b) / 2)


def uniform(a, b):
    return a + random.random() * (b - a)


def experimental(a, b, n):
    random_array = []
    for i in range(0, n):
        random_array.append(uniform(a, b))

    sum_total = 0

    for random_number in random_array:
        sum_total = sum_total + random_number

    mean = sum_total / n

    print("Practical expected value for even distribution between {0} and {1}:", a, b)
    print(mean)

    S = 0

    for random_number in random_array:
        S = S + (random_number - mean) ** 2

    S0 = (S / (n - 1)) ** 0.5

    print("Practical standard deviation for even distribution between {0} and {1}:", a, b)
    print(S0)


def main():
    """
    Variant 10.
    """

    a = 10
    b = 20
    n = 5000

    print("Count of random numbers: {0}", n)

    theoretical_standard_deviation()
    theoretical_expected_value(a, b)
    experimental(a, b, n)

main()
