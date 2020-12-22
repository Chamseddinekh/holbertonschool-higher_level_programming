#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def get_width(self):
        """getter of width"""
        return self.__width

    def set_width(self, width):
        """setter of width"""
        self.__width = width

    @property
    def get_height(self):
        """getter of height"""
        return self.__height

    def set_height(self, height):
        """setter of height"""
        self.__height = height

    @property
    def get_x(self):
        """getter of x"""
        return self.__x

    def set_x(self, x):
        """setter of x"""
        self.__x = x

    @property
    def get_y(self):
        """getter of y"""
        return self.__y

    def set_y(self, y):
        """setter of y"""
        self.__y = y
