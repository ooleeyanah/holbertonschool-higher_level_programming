#!/usr/bin/python3
"""
A module that defines a square importing from 9-rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Instantiation with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
