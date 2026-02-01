#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The module contains a function that divides all elements of a matrix
by a given divisor and returns a new matrix with the results rounded
to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    This function takes a matrix (list of lists) and divides all elements
    by the given divisor. All elements are rounded to 2 decimal places.
    Returns a new matrix without modifying the original.

    Args:
        matrix (list): A list of lists containing integers or floats.
                      Each row must have the same size.
        div (int or float): The divisor. Must be a number and cannot be zero.

    Returns:
        list: A new matrix with all elements divided by div and rounded
              to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to zero.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided([[2, 4], [6, 8]], 2)
        [[1.0, 2.0], [3.0, 4.0]]
    """
    # Error message for matrix type validation
    type_error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(type_error_msg)

    # Check if matrix is empty
    if not matrix:
        raise TypeError(type_error_msg)

    # Check if each element is a list and validate contents
    first_row_size = None
    for i, row in enumerate(matrix):
        # Check if row is a list
        if not isinstance(row, list):
            raise TypeError(type_error_msg)

        # Check if row is empty
        if not row:
            raise TypeError(type_error_msg)

        # Set first row size for comparison
        if first_row_size is None:
            first_row_size = len(row)

        # Check if all rows have the same size
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all elements in row are numbers
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(type_error_msg)

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided elements rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            new_row.append(round(result, 2))
        new_matrix.append(new_row)

    return new_matrix
