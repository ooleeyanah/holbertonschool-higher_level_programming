#!/usr/bin/python3
"""
Defines a function that returns obj from JSON string.
"""
import json


def from_json_string(my_str):
    """Function to return object from JSON string. """
    return json.loads(my_str)
