#!/usr/bin/python3
"""
A module returns Boolean if obj is instance inherited from class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is inst of inheritance of class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
