"""
Prog:   Lab2.py
Auth:   Oleksii Krutko, IO-z91
Desc:   Theory of probability Lab 2. 2020
"""

import random


def theoretical_expected_value(a, b):

    M_x2 = (((b)**3)/3 - ((a)**3)/3)**0.5
    M_x = (((b) ** 2) / 2 - ((a) ** 2) / 2)**0.5

    D_x = (M_x2 - M_x**2)**0.5

    print("Theoretical expected value for even distribution between {0} and {1}:", a, b)
    print(M_x)

    print("Theoretical standard deviation for even distribution:")
    print(D_x)


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

    S_shift = (S / n) ** 0.5

    S_not_shift = (S / (n - 1)) ** 0.5

    print("Practical not shifted standard deviation for even distribution between {0} and {1}:", a, b)
    print(S_not_shift)

    print("Practical shifted standard deviation for even distribution between {0} and {1}:", a, b)
    print(S_shift)


def main():
    """
    Variant 10.
    """

    a = 10
    b = 20
    n = 5000

    print("Count of random numbers: {0}", n)

    theoretical_expected_value(a, b)
    experimental(a, b, n)


main()
