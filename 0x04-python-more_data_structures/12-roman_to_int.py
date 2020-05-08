#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string is None or '':
        return 0
    roman_number_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        if i in roman_number_dict:
            number += roman_number_dict[i]
    return number
