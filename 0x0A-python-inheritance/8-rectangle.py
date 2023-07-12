#!/usr/bin/python3

"""Defines a rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Takes inheritance from BaseGeometry

    inheritance:
        it inherit from BaseGeometry
    """

    def __init__(self, width, height):
        """
            Initialize the instance

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width
