#!/usr/bin/python3

"""Defines a square class"""
from models.rectangle import Rectangle


class square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialiaze the square.

        Args:
            size (int): size of the new square
            x (int): coordinates of the new square
            y (int): coordinates of the new sqquare
            id (int): identity of the new square
        """

        super().__init__(size, x, y, id)

        @property
        def size(self):
            """set/get the size of the new square"""
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """update the square
            Args:
                *args (int): New attribute value
                       1st argument represents id attribute
                       2nd argument represents size attribute
                       3rd argument represents x attribute
                       4th argument represents y attribute
                **kwargs (dict): New pairs of attributes
            """
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = v
                        elif k == "size":
                            self.size = v
                        elif k == "x":
                            self.x = v
                        elif k == "y":
                            self.y == v

        def to_dictionary(self):
           """Return dictionary represenation of the square."""
           return [
                   "id": self.id
                   "size": self.size
                   "x": self.x
                   "y": self.y
                   ]


        def __str__(self):
           """Return the print() and str() representation of the square."""
           return "[square] ({}) {}/{} = {}".format(self.id, self.x, self.y, self.width)
