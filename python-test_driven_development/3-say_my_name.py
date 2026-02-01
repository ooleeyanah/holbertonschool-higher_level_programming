#!/usr/bin/python3
"""
This module provides a function to print names in a formatted way.

The module contains a function that takes a first name and optional last name
and prints them in the format "My name is <first_name> <last_name>".
It includes type checking to ensure both parameters are strings.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): The first name
        last_name (str): The last name
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
