#!/usr/bin/python3

"""Defines a function that reads a file for 0-read_file.py"""


def read_file(filename=""):
    """Function that reads a file
    Args:
    filename:
    the file to be read

    return:
    prints the file to stdout
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end'')
