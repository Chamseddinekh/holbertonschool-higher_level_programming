#!/usr/bin/python3
"""unction that prints a text with 2 new lines
   after each of these characters: ., ? and :"""


def text_indentation(text):
    """unction that prints a text with 2 new lines
       after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    text = text.split("\n")
    for i in range(0, len(text)):
        print("{:s}".format(text[i].strip()))
