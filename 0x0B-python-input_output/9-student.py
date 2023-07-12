#!/usr/bin/python3

"""
it is the module for 9-student.py
"""


class Student:
    """it is a student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initialization

        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ public instance"""
    def to_json(self):
        return self.__dict__
