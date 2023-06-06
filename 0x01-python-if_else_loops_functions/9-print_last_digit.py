#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """Print the last digit of a number and return it."""
    print(abs(number) % 5, end="")
    return (abs(number) % 5)
