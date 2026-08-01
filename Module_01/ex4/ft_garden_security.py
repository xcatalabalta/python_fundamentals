#!/usr/bin/env python3
class Plant:
    """
    A class to represent a plant in the garden.
    A plant that can have a name, a height, an age and a growth rate.
    Methods: growth and aging.
    New method: create from a dictionary.
    All flake8 and mypy compliant.
    """
    def __init__(self, name="wtf?", height=0, age=0, growth=1):
        """
        Initialize a new Plant instance with given values
        Args:
            name (str): Name is capitalized,
            height (int/float): Height is in centimeters,
            Negative values for height and age are set to 0.
            age (int/float): Age is in days
            Negative values for age are set to 0.
            rounded to the nearest whole number to ensure it is an integer.
            growth (int/float): Growth is the amount by which the plant grows
            each time the grow method is called.
            Negative values for growth are set to 1.
        Returns:
            _type_: None
        Included guards to protect against invalid values.
        """
        self.name = name.capitalize() if isinstance(name, str) else "Wtf?"
        self._height = height if isinstance(height, (int, float))\
            and height >= 0 else 0
        self._age_days = round(age) if isinstance(age, (int, float))\
            and age >= 0 else 0
        self._growth = growth if isinstance(growth, (int, float))\
            and growth >= 0 else 1

    def show(self):
        """
        Display the plant's name, height, and age in a formatted string.
        The age is displayed in singular or plural form based on its value.
        Returns:
            _type_: None
        """
        print(f"{self.name}: {self._height}cm, {self._age_days} "
              f"{'day' if self._age_days == 1 else 'days'} old")

    def grow(self, growth=None):
        """
        Increase the height of the plant by the specified growth amount.
        The growth amount must be a positive number.
        Otherwise, the height remains unchanged.
        If growth is None, the plant grows by its default growth rate.
        Args:
            growth (int/float): The amount by which the plant should grow.
        Returns:
            _type_: None
        """
        if isinstance(growth, (int, float)) and growth > 0:
            self._height += growth
        else:
            if growth is None:
                self._height += self._growth

    def age(self, days=1):
        """
        Increase the age of the plant by the specified number of days.
        The days must be a positive number.
        Otherwise, the age remains unchanged.
        Age is rounded to the nearest whole number to ensure it is an integer.
        Age calls the grow method.
        Args:
            days (int/float): Number of days to age the plant.
        Returns:
            _type_: None
        """
        if isinstance(days, (int, float)) and days > 0:
            self._age_days += round(days)
            for _ in range(round(days)):
                self.grow()
        else:
            print(f"{self.name}: Error, aging must be a positive number.")
            print("Update rejected.")

    def set_height(self, new_height):
        """
        Set the height of the plant to a new value.
        The new height must be a positive number.
        Otherwise, the height remains unchanged.
        Args:
            new_height (int/float): The new height value.
        Returns:
            _type_: None
        """
        if isinstance(new_height, (int, float)) and new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        elif isinstance(new_height, (int, float)) and new_height < 0:
            print(f"{self.name}: Error, height cannot be negative.")
            print("Update rejected.")
        else:
            print(f"{self.name}: Error, height must be a number.")
            print("Update rejected.")

    def set_age(self, new_age):
        """
        Set the age of the plant to a new value.
        The new age must be a positive number.
        Otherwise, the age remains unchanged.
        Age is rounded to the nearest whole number to ensure it is an integer.
        Args:
            new_age (int/float): The new age value.
        Returns:
            _type_: None
        """
        if isinstance(new_age, (int, float)) and new_age >= 0:
            self._age_days = round(new_age)
            print(f"Age updated: {self._age_days} days")
        elif isinstance(new_age, (int, float)) and new_age < 0:
            print(f"{self.name}: Error, age cannot be negative.")
            print("Update rejected.")
        else:
            print(f"{self.name}: Error, age must be a number.")
            print("Update rejected.")

    def set_growth(self, new_growth):
        """
        Set the growth rate of the plant to a new value.
        The new growth rate must be a positive number.
        Otherwise, the growth rate remains unchanged.
        Args:
            new_growth (int/float): The new growth rate value.
        Returns:
            _type_: None
        """
        if isinstance(new_growth, (int, float)) and new_growth >= 0:
            self._growth = new_growth
            print(f"Growth rate updated: {self._growth}cm per growth cycle")
        elif isinstance(new_growth, (int, float)) and new_growth < 0:
            print(f"{self.name}: Error, growth rate cannot be negative.")
            print("Update rejected.")
        else:
            print(f"{self.name}: Error, growth rate must be a number.")
            print("Update rejected.")

    def get_height(self):
        """
        Get the current height of the plant.
        Returns:
            _type_: float
        """
        return self._height

    def get_age(self):
        """
        Get the current age of the plant.
        Returns:
            _type_: int
        """
        return self._age_days

    def get_growth(self):
        """
        Get the current growth rate of the plant.
        Returns:
            _type_: float
        """
        return self._growth


def creation(plant_list: list[dict]) -> list[Plant]:
    """
    Create plants from a list of dict corresponding to plants
    Defined as static method can be called without an instance of the class.
    Defined as a regular function can be called outside the class.
    Args:
        plant_list (list[dict]): a list of dictionaries (typed as list[dict])
        Invalid and missing values are handled by the Plant class constructor.
    Returns:
        _type_: list of Plant objects
    Alternatively, this function can be defined as a static method.
    # @staticmethod
    # def creation(plant_list: list[dict]) -> list["Plant"]:
    """
    plants = []
    for plant_dict in plant_list:
        name = plant_dict.get('name')
        height = plant_dict.get('height')
        age = plant_dict.get('age')
        growth = plant_dict.get('growth')
        plant = Plant(name, height, age, growth)
        plants.append(plant)
    return plants


valid = 25
invalid = -5
thing = "some"
print("=== Garden Security System ===")
rose = Plant("Rose", 15.0, 10, 2.0)
print("Plant created: ", end='')
rose.show()
print(f"Growth rate of {rose.name}: {rose.get_growth()}cm per grow() call")
rose.set_height(valid)
rose.set_age(valid + 5)
print("Current state: ", end='')
rose.show()
print("=== Invalid Updates ===")
rose.set_height(invalid)
rose.set_age(invalid)
rose.set_height(thing)
rose.set_age(thing)
print("Current state: ", end='')
rose.show()
# Un/comment the following lines to test getters:
# print(f"Height: {rose._height()}cm")
# print(f"Age: {rose._age_days()} days")
# print(f"Height: {rose.get_height()}cm")
# print(f"Age: {rose.get_age()} days")
rose.age(valid)
print(f"Current state after aging {valid} days: ", end='')
rose.show()
print(f"Trying to get back to the original age by aging -{valid} days:")
rose.age(-valid)
print(f"Current state after aging -{valid} days: ", end='')
rose.show()
