#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.width = size
