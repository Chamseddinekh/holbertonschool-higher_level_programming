#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        if super().integer_validator('width', width):
            self.__width = width

        if super().integer_validator('height', height):
            self.__height = height

    def area(self):
        """
        Area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print Area
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
