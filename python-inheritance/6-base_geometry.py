#!/usr/bin/python3
"""
A module that passes an unfinished class.
"""


class BaseGeometry:
    """
    Raise exception about area.
    """
    def area(self):
        raise NotImplementedError("area() is not implemented")
