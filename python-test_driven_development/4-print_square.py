#!/usr/bin/python3
"""
This module provides a function to print squares using the '#' character.

The module contains a function that prints a square of a given size
using the '#' character. It includes validation to ensure the size
is a non-negative integer.
"""


def print_square(size):
    """Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int) or isinstance(size, bool):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
