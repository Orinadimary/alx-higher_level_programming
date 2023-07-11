#!/usr/bin/python3
"""Defines inherited lists from mylist"""

Class MyList(list):
    """Takes inheritance from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(self))
