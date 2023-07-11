#!/usr/bin/python3

"""Module for 5-save_to_json_file.py"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file

    Args:
    my_obj: object the file will be written to
    Filename: file to be written to

    return:
    filename with JSON representation
    """

    with open(filename, 'w', encoding='utf-8') as f:
        content = json.dumps(my_obj)
        save = f.write(content)
        return save
