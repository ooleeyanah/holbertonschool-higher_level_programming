#!/usr/bin/python3
"""
Defines a function that writes an obj to a txt file with JSON rep.
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function to save object to file with JSON rep. """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
