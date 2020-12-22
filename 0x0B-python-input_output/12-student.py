#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """
    class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        if attrs:
            for i in self.__dict__.items():
                for j in i:
                    if j in attrs:
                        return dict([i])
        else:
            return self.__dict__
