#!/usr/bin/env python3
class Plant:
    """
    A class to represent a plant in the garden.
    A plant that can have a name, a height and an age.
    All flake8 compliant.
    """
    def __init__(self, name="wtf?", height=0, age=0):
        """
        Initialize a new Plant instance.
        name is capitalized,
        height is in centimeters, and age is in days.
        Incldued guards to protect against invalid values.
        """
        self.name = name.capitalize() if isinstance(name, str) else "Wtf?"
        self.height = height if isinstance(height, (int, float))\
            and height > 0 else 0
        self.age = age if isinstance(age, (int, float)) and age > 0 else 0

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


print("=== Testing ===")
rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 150, 10)
cactus = Plant("Cactus", 15, 100)
hibiscus = Plant("hibiscus", 30, 20)
print("=== Garden Plant Registry ===")
rose.show()
sunflower.show()
cactus.show()
hibiscus.show()
print("=== Testing Default and Invalid Values ===")
kosa = Plant()
print("Empty plant")
kosa.show()
print("Invalid values:")
tupe = Plant("Tupe", -10, -5)
print("tupe = Plant(\"Tupe\", -10, -5)")
tupe.show()
print("moko = Plant(123, 50, 10)")
moko = Plant(123, 50, 10)
moko.show()
cardo = Plant("Cardo", '', "five")
print("cardo = Plant(\"Cardo\", '', \"five\")")
cardo.show()
print("Height is a valid value from a variable:")
h = 84
cardo = Plant("Cardo", h, 3)
cardo.show()
expe = Plant("Expe", True, True)
print("expe = Plant(\"Expe\", True, True)")
expe.show()
print("The instance rosita = Plant(rose) has not been created")
rosita = Plant(rose)
rosita.show()
print(
    "The type of the instance is:"
    f" {type(rosita).__name__}  ")
