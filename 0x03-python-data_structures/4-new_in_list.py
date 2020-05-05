#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = list(my_list)
    if idx < 0 or idx > length:
        return my_list
    for i in range(length):
        if idx == i:
            new_list[i] = element
    return new_list
