#!/usr/bin/python3
"""
Module that uses xml to serialize and deserialize.

"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file back to a Python dict.

    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            value = child.text

            if value is not None:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
            dictionary[child.tag] = value
        return dictionary
    except (ET.ParseError, FileNotFoundError):
        return {}
