#!/usr/bin/python3
"""
Verbose list class to extend python list class.
"""

class VerboseList(list):
    """
    Class to override list modification funcs.
    """
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")
    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    def pop(self, index=None):
        if index is None:
            popped_item = super().pop()
        else:
            popped_item = super().pop(index)
        print(f"Popped [{popped_item}] from the list.")
        return popped_item

if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
