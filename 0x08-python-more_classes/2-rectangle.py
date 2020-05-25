#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines Rectangle Class"""
    def __init__(self, width=0, height=0):
        """
        constructeur
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter heigth
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Area of rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        perimetre of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
