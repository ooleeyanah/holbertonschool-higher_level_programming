#!/usr/bin/python3
"""
Module that defines a function that serializes and deserializes.

"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    """
    with open(filename, 'r') as file:
        return json.load(file)