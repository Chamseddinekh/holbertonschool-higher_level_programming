#!/usr/bin/python3
"""
Fuction that read file
"""


def read_file(filename=""):
    """
    Read File
    """
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end="")
