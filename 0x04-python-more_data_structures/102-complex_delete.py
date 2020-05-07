#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary
    for x in list(new_dict):
        if new_dict[x] == value:
            del new_dict[x]
    return new_dict
