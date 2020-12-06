#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
   function that writes a string to a text file
    """
     with open(filename, 'r', encoding='utf8') as f:
         return f.write(text)
