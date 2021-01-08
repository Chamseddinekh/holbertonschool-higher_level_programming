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
        return self.size

    @size.setter
    def y(self, y):
        """setter of size"""
        if type(y) is not int:
            raise TypeError("size must be an integer")
        if y < 0:
            raise ValueError("size must be >= 0")
        self.size = self.width
        self.size = self.height
