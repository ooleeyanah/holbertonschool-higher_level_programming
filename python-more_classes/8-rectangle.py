#!/usr/bin/python3
"""
Module that defines a Rectangle class.

"""


class Rectangle:
    """
    A class that represents a rectangle.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle instance.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def print(self):
        """
        Print the rectangle using the '#' character.

        """
        if self.width == 0 or self.height == 0:
            print()
            return
        for _ in range(self.__height):
            print(str(self.print_symbol) * self.__width)

    def __str__(self):
        """
        Print the rectangle using the '#' character.

        """
        if self.width == 0 or self.height == 0:
            return ""
        result = []
        for _ in range(self.__height):
            result.append(str(self.print_symbol) * self.__width)
        return '\n'.join(result)

    def __repr__(self):
        """
        Print the rectangle using the '#' character.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Delete rectangle with a bittersweet goodbye.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares rectangles and returns biggest.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
