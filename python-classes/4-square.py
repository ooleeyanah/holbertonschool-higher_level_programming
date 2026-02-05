#!/usr/bin/python3
"""
Module that defines a Square class with size property validation.

"""


class Square:
    """
    A class that represents a square with property-based size validation.
    
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        """
        return self.__size ** 2
