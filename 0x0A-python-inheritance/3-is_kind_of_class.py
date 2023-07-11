#!/usr/bin/python3

"""Defines a functions that checks class"""

def is_kind_of_class(obj, a_class):
    """checks if the object in the instance and the class are the same.

    Args:
    obj: Object to check
    a_class: the class that shpuld be with the object

    Returns:
    True - if obejct is as the a_class, Otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
