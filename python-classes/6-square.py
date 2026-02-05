#!/usr/bin/python3
"""
Module that defines a Square class with size and position properties.

"""


class Square:
    """
    A class that represents a square with size and position properties.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with size and position.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character with position offset.

        """
        if self.__size == 0:
            print()
            return


        for _ in range(self.__position[1]):
            print()


        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
