#!/usr/bin/python3
"""
A script to add all args to a list then save as file.
"""
import sys
from importlib import import_module

save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = import_module('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
