#!/usr/bin/python3

"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangl.
        Args:
        width (int): width of the new Rectangle
        height (int): height of the new Rectangle
        y (int):  coordinates of the rectangle
        x (int): coordinates of the new rectangle
        id (int): identity of the new rectangle

        Raises:
        TypeError: if width or height is not int.
        ValueError: if either the width or the height is <=0.
        TypeError: if either x  or y is not an int
        ValueError: if either x or y < 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            return TypeError("width must be an integer")
        if value <= 0:
            raise ValueError(width must be > 0")
            self.__width = value                            
