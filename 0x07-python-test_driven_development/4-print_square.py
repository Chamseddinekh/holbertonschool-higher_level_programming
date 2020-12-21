#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """
    function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
