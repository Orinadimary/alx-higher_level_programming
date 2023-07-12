#!/usr/bin/python3

"""Defines a function that checks True or Fslse"""


def inherits_from(obj, a_class):


"""checks if objects is  in a given class.

    Args:
    obj: Object to check
    a_class: the class that shpuld be with the object

    Returns:
    True - if obejct is as the a_class, Otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
