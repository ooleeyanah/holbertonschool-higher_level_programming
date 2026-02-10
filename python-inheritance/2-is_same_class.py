#!/usr/bin/python3
"""
A module that returns Boolean if obj is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance of specified class.
    """
    return type(obj) is a_class
