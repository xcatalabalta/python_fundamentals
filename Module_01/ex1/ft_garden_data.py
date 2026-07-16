#!/usr/bin/env python3
class Plant:
    """
    A class to represent a plant in the garden.
    A plant that can have a name, a height and an age
    """
    def __init__(self, name, height, age):
        """
        Initialize a new Plant instance.
        """
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 150, 10)
cactus = Plant("Cactus", 15, 100)
hibiscus = Plant("hibiscus", 30, 20)
print("=== Garden Plant Registry ===")
rose.show()
sunflower.show()
cactus.show()
hibiscus.show()
