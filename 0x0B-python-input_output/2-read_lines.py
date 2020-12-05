#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
   reads n lines of a text file
    """
    i = 0
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            if i == nb_lines and nb_lines != 0:
                break
            print(line, end="")
            i += 1

