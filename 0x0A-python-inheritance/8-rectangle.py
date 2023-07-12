#!/usr/bin/python3

"""Defines a rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a class using basegeometry"""

    def __init__(self, width, height):
        """initialize a new rectangle
            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width
