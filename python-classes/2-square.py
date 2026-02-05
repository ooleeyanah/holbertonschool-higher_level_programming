#!/usr/bin/python3
"""
Module that defines a Square class with size validation.
This module contains a Square class that validates the size attribute
to ensure it's a non-negative integer.
"""


class Square:
    """
    A class that represents a square with validated size attribute.
    
    This class defines a square by storing its size as a private attribute
    with proper validation to ensure the size is a non-negative integer.
    This prevents invalid square dimensions and maintains data integrity.
    
    Attributes:
        __size (int): Private attribute that stores the size of the square.
                     Must be a non-negative integer.
    
    Methods:
        __init__(self, size): Initializes a new Square instance with 
                             validated size.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    
    def __init__(self, size=0):
        """
        Initialize a new Square instance with size validation.
        
        This constructor creates a new Square object with the specified size.
        The size is validated to ensure it's a non-negative integer before
        being stored as a private attribute.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
                                 Must be a non-negative integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative (less than 0).
        
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
