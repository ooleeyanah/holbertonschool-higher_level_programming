#!/usr/bin/python3
"""
Defines a function that returns dict desc for JSON serialisation.
"""


def class_to_json(obj):
    """ Function to return dict for JSON serialisation of obj. """
    return obj.__dict__
