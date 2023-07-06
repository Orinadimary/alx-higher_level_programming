#!/usr/bin/python3
"""Modulethat finds the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    d = 1
    while d < len(list):
        if list[d] > result:
            result = list[d]
        d += 1
    return result
