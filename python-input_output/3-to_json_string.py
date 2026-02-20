#!/usr/bin/python3
"""
Defines a function that returns JSON rep of obj.
"""
import json

def to_json_string(my_obj):
    """ Function to return JSON rep of obj. """
    json_string = json.dumps(my_obj)
    return(json_string)
