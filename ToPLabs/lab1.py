"""
Prog:   Lab1.py
Auth:   Oleksii Krutko, IO-z91
Desc:   Theory of probability Lab 1. 2020
"""

import random
import math


def are_A_and_B_in_different_team_with_C(pull_of_players, A, B, C):
    team_of_A = (pull_of_players.index(A)) // 6
    team_of_B = (pull_of_players.index(B)) // 6
    team_of_C = (pull_of_players.index(C)) // 6
    return team_of_A == team_of_B and team_of_C != team_of_A


def analytical():
    # Probability that C is one of the teams is 100%

    # Probability that A is in another team
    # (Number of places in another team) / (total places - place of C)
    A_in_diff_team = 6 / (12 - 1)

    # Probability that B is in another team
    # (Number of places in another team - place of A) / (total places - place of C - place of A)
    B_in_diff_team = (6 - 1) / (12 - 1 - 1)

    # Probabilities are multiplied
    result = A_in_diff_team * B_in_diff_team

    return result


def monte_carlo(iterations_number):
    A = 1
    B = 2
    C = 3

    in_diff_teams_count = 0

    for i in range(0, iterations_number):
        pull_of_players = random.sample(range(1, 13), 12)

        if are_A_and_B_in_different_team_with_C(pull_of_players, A, B, C):
            in_diff_teams_count = in_diff_teams_count + 1

    analytical_result = analytical()

    print("Probability by analytic:")
    print(analytical_result)

    print("Probability by Monte-carlo with number of iterations:")
    print(iterations_number)
    print(in_diff_teams_count / iterations_number)

    print("Error is:")
    print(math.fabs((analytical_result - in_diff_teams_count / iterations_number)) / analytical_result)


def main():
    """
    Variant 10.
    """
    monte_carlo(100000)


main()
