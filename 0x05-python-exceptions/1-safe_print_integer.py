#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
    value (int): prints integer

    Returns:
    False, if a typeError or ValueError occurs
    Otherwise, True.

    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
