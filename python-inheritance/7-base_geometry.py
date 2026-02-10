#!/usr/bin/python3
"""
A module that passes an unfinished class.
"""


class BaseGeometry:
    """
    Raise exception about area.
    """
    def area(self):
        """
        Raises an Exception indicating area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer greater than zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
