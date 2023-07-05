#!/usr/bin/python3

"""
Defines a rectagle object
"""
class Rectangle:
    """
    Represents the Rectangle
    
    """
    def __init__(self, width=0, height=0):
        
        """
        initialize the new rectangle.
        Args:
            width (int): Width of the new Rectagle.
            Height (int): Height of the new Rectangle.
            """
            self.width=width
            self.height=height
            
    @property
    def width(self):
        """
        Gets the width of the instance.
        
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width of the rectangle.
        Parameters:
            value (int): The width of the rectangle.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Gets the width of the instance.
        
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the height of the rectangle.
        Parameters:
            value (int): The height of the rectangle.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
