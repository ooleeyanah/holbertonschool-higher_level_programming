#!/usr/bin/python3
"""
Module that defines Student class.

"""


class Student:
    """
    A class that represents a student.

    """

    def __init__(self, first_name, last_name, age):
        """ Initialize Student instance. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Public method to retrieve dict rep of Student. """
        return Student.__dict__
