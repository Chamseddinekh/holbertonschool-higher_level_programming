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
        if type(self.width) is not int:
            raise TypeError("size must be an integer")
        if self.width < 0:
            raise ValueError("size must be >= 0")
        self.width = size

    def update(self, *args, **kwargs):
        """update args"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        else:
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'size' in kwargs:
                    self.size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self): 
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
