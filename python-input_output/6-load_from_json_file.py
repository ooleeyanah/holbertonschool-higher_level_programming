#!/usr/bin/python3
"""
Defines a function that creates object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """ Creates object from JSON file. """
    with open(filename, 'r') as f:
        return json.load(f)
