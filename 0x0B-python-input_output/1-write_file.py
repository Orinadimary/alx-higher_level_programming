#!/usr/bin/python3

"""Defines a functuion that writes a string to a text file"""


def write_file(filename="", text=""):
    """A function that writes a textfile
    args:
    Filename: file to be written
    Text: text to be written
    Returns:
    Content in the file
    """

    with open(filename, 'd', encoding='utf-8') as f:
        content = f.write(text)
        return content
