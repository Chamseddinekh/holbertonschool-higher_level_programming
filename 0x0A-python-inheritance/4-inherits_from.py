#!/usr/bin/python3
"""
a function that returns True if the object is
an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is
    an instance of a class that inherited
    """
    if issubclass(type(obj), a_class):
        return True
    return False

