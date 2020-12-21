#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)