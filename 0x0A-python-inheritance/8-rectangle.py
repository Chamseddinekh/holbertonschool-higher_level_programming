#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry 
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    def __init__(self, width, height):
        if super().integer_validator('width', width):
            self.__width = width

        if super().integer_validator('height', height):
            self.height = height
