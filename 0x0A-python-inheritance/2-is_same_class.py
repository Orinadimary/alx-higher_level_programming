#!/usr/bin/python3

"""Defines a function that checks True or Fslse"""

def is_same_class(obj, a_class):
    """Checks if objects is  in a given class.

    Args:
    obj: Object to check
    a_class: the class that shpuld be with the object

    Returns:
    True - if obejct is as the a_class, Otherwise False.
    """
    if obj == a_class:
        return True
    return False
