#!/usr/bin/python3
from models.base import Base
"""
class Rectangle that inherits from Base
"""

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
        return self.__width

    def set_width(self, width):
        self.__width = width

    @property
    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    @property
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    @property
    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y
