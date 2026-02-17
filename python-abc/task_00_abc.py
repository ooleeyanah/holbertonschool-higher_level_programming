#!/usr/bin/python3
"""
Animal abstract method for sounds of a dog and cat.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Defines Animal class for abstract methods.
    """
    
    @abstractmethod
    def sound(self):
        """
        Sound abstract method.
        """
        pass

class Dog(Animal):
    """Dog class that inherits from Animal."""
    
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal."""
    
    def sound(self):
        return "Meow"
