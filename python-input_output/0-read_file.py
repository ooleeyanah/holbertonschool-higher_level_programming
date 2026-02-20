#!/usr/bin/python3
"""
Defines a function that reads a file.
"""

def read_file(filename=""):
    """ Read a file function. """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
