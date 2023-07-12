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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

      def area(self):
          """Return area of the rectangle"""
          return self.__width * self.__height

      def __str__(self):
          """Return the print() and str() representation"""
          string = "[" + str(self.__class__.__name__) + "]"
          string += str(self.__width) +"/" + str(self.__height)
          return string
