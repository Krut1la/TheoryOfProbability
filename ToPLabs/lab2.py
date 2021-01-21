"""
Prog:   Lab2.py
Auth:   Oleksii Krutko, IO-z91
Desc:   Theory of probability Lab 2. 2020
"""

import random


def theoretical_expected_value(a, b, c, h2_div_h1):

    h1 = 1 / ((b - a) + (c - b) * h2_div_h1)
    h2 = h2_div_h1 / ((b - a) + (c - b) * h2_div_h1)

    M_x = (h1 / 2) * (b**2 - a**2) + (h2 / 2) * (c**2 - b**2)

    D_x = (h1 / 3) * (b**3 - a**3) + (h2 / 3) * (c**3 - b**3) - M_x ** 2

    Q = D_x ** 0.5

    print("Theoretical expected value:")
    print(M_x)

    print("Theoretical dispersion:")
    print(D_x)

    print("Theoretical standard deviation:")
    print(Q)


def experimental(uniform2_random_array):
    sum_total = 0

    n = len(uniform2_random_array)

    for random_number in uniform2_random_array:
        sum_total = sum_total + random_number

    mean = sum_total / n

    print("Experimental expected value = {0}".format(mean))

    S = 0

    for random_number in uniform2_random_array:
        S = S + (random_number - mean) ** 2

    S_not_shift = (S / (n - 1)) ** 0.5

    print("Experimental standard deviation  = {0}".format(S_not_shift))


def generate_uniform2_random(random_array, a, b, c, h2_div_h1):
    uniform2_random_array = []

    for r in random_array:
        Rj = ((r * ((b - a) + h2_div_h1 * (c - b)) - b + a) / h2_div_h1) + b

        uniform2_random_array.append(Rj)

    return uniform2_random_array


def generate_input_random(n):
    random_array = []
    for i in range(0, n):
        random_array.append(random.random())

    return random_array


def main():
    """
    Variant 10.
    """

    a = 10.0
    b = 20.0
    c = 50.0
    h2_div_h1 = 2
    n = 50000

    uniform2_random_array = generate_uniform2_random(generate_input_random(n), a, b, c, h2_div_h1)

    print("Count of random numbers: {0}".format(n))
    print("Parameters of uniform double level sequence: a = {0}, b = {1}, c = {2}, h2_div_h1 = {3}".format(a, b, c, h2_div_h1))

    theoretical_expected_value(a, b, c, h2_div_h1)
    experimental(uniform2_random_array)


main()
