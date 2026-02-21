#!/usr/bin/python3
"""
Defines a function that creates object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """ Creates object from JSON file. """
    json.loads(filename)
