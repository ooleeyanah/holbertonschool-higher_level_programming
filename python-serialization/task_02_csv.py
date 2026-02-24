#!/usr/bin/python3
"""
Module that defines a custom class CustomObject.

"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts CSV file to JSON format and writes to data.json.

    """
    try:
        data = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, Exception):
        return False
