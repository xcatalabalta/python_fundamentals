#!/usr/bin/env python3
class Plant:
    """
    A class to represent a plant in the garden.
    A plant that can have a name, a height and an age.
    New methods have been added to allow for growth and aging of the plant.
    Age attribute has been renamed to age_days
    to avoid conflict with the age method.
    All flake8 and mypy compliant.
    """
    def __init__(self, name="wtf?", height=0, age=0, growth=1):
        """
        Initialize a new Plant instance.
        Name is capitalized,
        height is in centimeters, age is in days,
        growth is the amount by which the plant grows
        each time the grow method is called.
        Included guards to protect against invalid values.
        Negative values for height and age are set to 0.
        Negative and zero values for growth are set to 1.
        Age is rounded to the nearest whole number to ensure it is an integer.
        """
        self.name = name.capitalize() if isinstance(name, str) else "Wtf?"
        self.height = height if isinstance(height, (int, float))\
            and height > 0 else 0
        self.age_days = round(age) if isinstance(age, (int, float))\
            and age > 0 else 0
        self.growth = growth if isinstance(growth, (int, float))\
            and growth > 0 else 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self, growth=None):
        """
        Increase the height of the plant by the specified growth amount.
        The growth amount must be a positive number.
        Otherwise, the height remains unchanged.
        """
        if isinstance(growth, (int, float)) and growth > 0:
            self.height += growth
        else:
            if growth is None:
                self.height += self.growth

    def age(self, days=1):
        """
        Increase the age of the plant by the specified number of days.
        The days must be a positive number.
        Otherwise, the age remains unchanged.
        Age is rounded to the nearest whole number to ensure it is an integer.
        Age calls the grow method.
        """
        if isinstance(days, (int, float)) and days > 0:
            self.age_days += round(days)
            for _ in range(round(days)):
                self.grow()


print("=== Testing grow and age methods ===")
rose = Plant("Rose", 25, 30)
rose.show()
print("Positive growth value (5cm):")
rose.grow(5)
rose.show()
print("Negative growth value (-3cm):")
rose.grow(-3)
rose.show()
print("None growth value (default = 1cm):")
rose.grow()
rose.show()
print("Zero growth value:")
rose.grow(0)
rose.show()
print("Positive age value (10 days):")
rose.age(10)
rose.show()
print("Negative age value (-5 days):")
rose.age(-5)
rose.show()
print("None age value:")
rose.age()
rose.show()
print("Zero age value:")
rose.age(0)
rose.show()
print("=== Following the subject ===")
print("=== Garden Plant Growth ===")
rose = Plant("Rose", 25, 30)
rose.show()
print(f"Rose grows by {rose.growth}cm each time it grows.")
cardo = Plant("Cardo", 10, 5, 2)
cardo.show()
print(f"Cardo grows by {cardo.growth}cm each time it grows.")
a = cardo.age_days
print(f"Cardo is {a} days old.")
for _ in range(7):
    print(f"=== Day {_ + 1} ===")
    rose.age()
    rose.show()
    cardo.age()
    cardo.show()
