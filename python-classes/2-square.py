#!/usr/bin/python3
"""
Module that defines a Square class with size validation.

"""


class Square:
    """
    A class that represents a square with validated size attribute.

    """
    
    def __init__(self, size=0):
        """
        Initialize a new Square instance with size validation.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
