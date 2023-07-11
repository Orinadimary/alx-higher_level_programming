#!/usr/bin/python3

"""
Module for 2-append_write.py
"""


def append_write(filename="", text=""):
    """
    This function append text to filename

    Args:
        filename: file to create or append text to
        text: text to insert into filename

    Return:
        Number of character added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        content = f.write(text)
        return content
