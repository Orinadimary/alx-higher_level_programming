#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        the real number of elements printed
        """
    ret = 0
    for q in range(x):
        try:
            print("{}".format(my_list[q]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)