#!/usr/bin/python3
"""
This module provides a function to add two integers.

The module contains a function that adds two numbers (integers or floats)
and returns their sum as an integer. It includes type checking and
error handling for invalid input types.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    This function takes two numbers (int or float) and returns their sum
    as an integer. If either parameter is not an int or float, it raises
    a TypeError.
    
    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.
    
    Returns:
        int: The sum of a and b as an integer.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
