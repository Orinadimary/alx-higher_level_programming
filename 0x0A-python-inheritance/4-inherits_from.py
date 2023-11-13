#!/usr/bin/python3

"""
It is a module to inherit from function.
"""

def inherits_from(obj, a_class):
    """
    Inherits from function

    args:
    obj: object to check inheritance
    a_class: class object inherited from

    Return:
    boolean: True or False
    """

    if type(obj)== a_class:
        return False
    elif is instance(obj, a_class):
        return True 
    else:
        return False




