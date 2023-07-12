#!/usr/bin/python3

"""
module for the BaseGeomety class
"""


class BaseGeometry:
    """ its is a basegeometry class"""

    """ public instance"""
    def area(self):
        raise Exception("area() is not implemented")

    """ public instance
        Args:
            name: name of the variable
            value: name value

        Rises:
            TypeError: must be an int
            ValuError: name must be greater than 0
    """
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
