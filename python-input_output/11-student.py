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

    def to_json(self, attrs=None):
        """ Public method to retrieve dict rep of Student. """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """ Public method to replace all attrs of Student. """
        for key, value in json.items():
            setattr(self, key, value)
