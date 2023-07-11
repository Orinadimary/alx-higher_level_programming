#!/usr/bin/python3

"""Module for 4-from_json_string.py"""

import json


def from_json_string(my_str):
    """function returns object that represented by json string"""
    return json.get(my_str)
