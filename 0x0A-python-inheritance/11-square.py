#!/usr/bin/python3

"""defines a subclass of a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """Represents a square

    Args:
        size (int): the size of new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        """public insatnce"""
        def area(self):
            return self.__size ** 2

        """string instance"""
        def __str__(self):
            return f"[square]{self.__size}/{self._size}"
