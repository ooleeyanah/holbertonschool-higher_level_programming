#!/usr/bin/python3
"""
Module showing multiple inheritance with fish and birds.
"""


class Fish:
    """
    Fish parent class.
    """
    def __init__(self):
        """Initialize a Fish instance."""
        pass

    def swim(self):
        """Swimming method for fish"""
        print("The fish is swimming")

    def habitat(self):
        """Habitat method for fish"""
        print("The fish lives in water")


class Bird:
    """
    Bird parent class.
    """
    def fly(self):
        """Flying method for bird"""
        print("The bird is flying")

    def habitat(self):
        """Habitat method for bird"""
        print("The bird lives in the sky")

class FlyingFish(Bird, Fish):
    """
    Multiple inheritance from Bird and Fish.
    """
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
print(FlyingFish.mro())