#!/usr/bin/python3

"""Definess a function that reads UTF text file"""


def read_file(filename=""):
    """Function that reads a test file UTF.
    Args:
    Filename: the file to be read

    Returns: prints the file to stdout
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end'')
