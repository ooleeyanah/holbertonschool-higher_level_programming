#!/usr/bin/python3
"""
A module that defines a Rectangle class inheriting from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height.
        
        Args:
            width (int): width of the rectangle (must be positive integer)
            height (int): height of the rectangle (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
