#!/usr/bin/python3
"""
This module provides a function for text indentation formatting.

The module contains a function that formats text by adding two new lines
after specific punctuation characters (., ?, :) and removes any leading
spaces after these characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): The text to be indented.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent_chars = {'.', '?', ':'}
    result = []
    i = 0
    length = len(text)

    while i < length:
        result.append(text[i])
        if text[i] in indent_chars:
            result.append('\n\n')
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(''.join(result), end='')
