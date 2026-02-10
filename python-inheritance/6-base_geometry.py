#!/usr/bin/python3
"""
A module that passes an unfinished class.
"""


class BaseGeometry:
    """
    Raise exception about area.
    """
    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
