#!/usr/bin/python3
"""
Defines a function that appends then counts chars.
"""


def append_write(filename="", text=""):
    """ Append a file function. """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
