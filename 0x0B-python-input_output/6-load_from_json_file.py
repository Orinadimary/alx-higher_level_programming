#!/usr/bin/python3

"""Module for 6-load_from_json_file.py"""

import json


def load_from_json_file(filename):
    """Function creates object frm json file

    Args:
    Filename: file to load from

    return:
    JSON file that was loaded
    """

    with open(filename, encoding='utf-8') as f:
        content = f.read()
        load = json.loads(content)
        return load
