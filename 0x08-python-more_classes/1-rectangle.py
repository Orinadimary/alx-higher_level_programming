#!/usr/bin/python3

"""
Defines a Rectangle Object.
"""

Class Rectangle:
    """

    """Represents the Rectangle."""

    def__init__(self, width=0, height=0):
        """initialize the new triangle."""

        Args:
            width (int): Width of the new Rectagle.
            Height (int): Height of the new Rectangle.
            """
            self.width = width
            self.height = height

            @property
            def width(self):
            """set width of the Rectangle."""
            return self.__width

            @width.setter
            def width(self, value):
            if not isinstance(value, int):
            raise TypeError("width must be integer")
            if value < 0
            raise valueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
            """set height of Rectangle."""
            return self.__height

            @height.setter
            def height(self, value):
            if not isinstance(value, int):
            raise TypeError("Height must be integer")
            if value < 0:
            raise valueError("Height must be integer")
            self.__height = value
