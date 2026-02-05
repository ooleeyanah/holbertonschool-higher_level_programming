#!/usr/bin/python3
"""
Module that defines a Square class with private size attribute.
This module contains a Square class that encapsulates the size attribute
to maintain control over the square's dimensions.
"""


class Square:
    """
    A class that represents a square with a private size attribute.
    
    This class defines a square by storing its size as a private attribute,
    which allows for better control over the square's dimensions and
    prevents direct external access to the size value.
    
    Attributes:
        __size (int): Private attribute that stores the size of the square.
                     The double underscore prefix makes it name-mangled
                     and effectively private.
    
    Methods:
        __init__(self, size): Initializes a new Square instance with given size.
    """
    
    def __init__(self, size):
        """
        Initialize a new Square instance.
        
        This constructor creates a new Square object with the specified size.
        The size is stored as a private attribute to maintain encapsulation
        and control over the square's dimensions.
        
        Args:
            size: The size of the square. No type or value verification
                 is performed at this stage.
        
        Returns:
            None
        """
        self.__size = size
    