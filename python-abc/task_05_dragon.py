#!/usr/bin/python3
"""
Module showing mixin classes for a dragon.
"""

class SwimMixin:
    """
    Swim method for dragon to inherit.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Fly method for dragon to inherit.
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from fly and swim.
    """
    def roar(self):
        """
        Method for dragon to roar.
        """
        print("The dragon roars!")



if __name__ == "__main__":

    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()
