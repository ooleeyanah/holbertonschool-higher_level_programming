#!/usr/bin/python3
"""
Module to extend iter functionalities.

"""


class CountedIterator:
    """
    iter extension class that counts the number of items iterated.

    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable

        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Override __next__ method to increment counter and return next item.

        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Return the current count of items that have been iterated over.

        """
        return self.count
