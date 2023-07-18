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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the coordinate x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the coordinates y of the rectyangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) !=int:
            raise TypeError("y must be integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the "#" character."""
        if self.width == 0 or self.height == 0:
            print ""
            return 

    [print("") for y in range(self.y)]
    for h in range(self.height):
        [print(" ", end="") for x in range(self.x)]
        [print("#", end="") for w in range(self.width)]
        print("")

    def update(self, *args, **kwargs):
        """update the rectangle.
        Args:
            *args (ints): New value attribute
            1st argument represents id attribute
            2nd argument represents width attribute
            3rd argument represents heightattribute
            4th argument represents x attribute
            5th argument represents y attribute
        ***kwargs (dict): New pairs of attribute
        """

        if args and len(args) != 0:
            a = 0
            if a == 0:
                if arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.width, self.heigh, self.x, self.y)
                        else:
                            self.id = arg
                    elif a == 1:
                        self.width = arg
                    elif a == 2:
                        self.height = arg
                    elif a == 3:
                        self.x = arg
                    elif a == 4:
                        self.y == arg
                    a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        def to_dictionary(self):
            """Return the dictionary representation of the recatngle."""
            return {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                    }

        def __str__(self):
            """Return the print() and str() representation of the recatngle."""
            return "[Rectangle] ({}) {}/{}".format(self.id, self.width, self.height, self.x, self.y)
