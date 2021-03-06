#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to json"""
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + '.json'
        lst = []
        if list_objs is not None:
            for i in list_objs:
                lst.append(i)
        with open(file_name, 'w') as f:
            f.write(cls.to_json_string(lst))
