#!/usr/bin/python3

"""Define a rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class square (Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """initialize the new size

        Args:
        size (int): size of new square
        """
        self.integer_validator("size", size)
        super().__init(size, size)
        self.__size = size
