#!/usr/bin/python3
"""
Base Class
"""


class Base:
    """
    Base Class
    """
    def __init__(self, id=None):
        __nb_objects = 0
        if id:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
