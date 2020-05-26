#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines Rectangle Class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        constructeur
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter heigth
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Area of rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        perimetre of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        print rectangle
        """
        string = ''
        if self.height == 0 or self.width == 0:
            return ''
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i == self.height - 1:
                break
            string += '\n'
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
