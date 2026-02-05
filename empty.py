#!/usr/bin/python3
import sys

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Hello Jonathan, my name is {(self.name)}!")

    @property
    def name(self):
        print("Get the name.")
        return self._name
    
    @name.setter
    def name(self, newName):
        print("Set the name.")
        self._name = newName.capitalize()
    
    def __str__(self):
        return(f"You got me: {self._name} {hex(id(self))}")
    
    def __del__(self):
        print(f"{self._name} is leaving the class.")
        
    def __add__(student1, student2):
        print("Adding student.")
        return(Student(f"{student1._name}{student2._name}")) 

class Cohort28(Student):
    def __init__ (self, name):
        super().__init__(name)
        print("We are very noisy!")
        
def main():
   # print("Hello, World!")
    #matt = Student("matt")
    #lachie = Student("Lachie")
    #s = matt + lachie
    #print(s)
    #print(f"Matt's ID: {hex(id(matt))}")
    #print(f"Lachie's ID: {hex(id(lachie))}")
   # anon = matt
    #lachie._name = "Golden Legs"
   # print(f"Anon's ID: {hex(id(anon))}")
    #print(f"Matt's reference count: {sys.getrefcount(matt)}")
    #print(f"Lachie's reference count: {sys.getrefcount(lachie)}")
    #print(f"Anon's reference count: {sys.getrefcount(anon)}")
    #print(f"Lachie's new name is {lachie._name}.")
    #print(matt)
    s = Student("Sebastion")
    c = Cohort28("Uliana")


if __name__ == "__main__":
    main()
