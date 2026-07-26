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
        Initialize a new Plant instance.
        Name is capitalized,
        height is in centimeters, age is in days,
        growth is the amount by which the plant grows
        each time the grow method is called.
        Included guards to protect against invalid values.
        Negative values for height and age are set to 0.
        Negative values for growth are set to 1.
        Age is rounded to the nearest whole number to ensure it is an integer.
        """
        self.name = name.capitalize() if isinstance(name, str) else "Wtf?"
        self.height = height if isinstance(height, (int, float))\
            and height >= 0 else 0
        self.age_days = round(age) if isinstance(age, (int, float))\
            and age >= 0 else 0
        self.growth = growth if isinstance(growth, (int, float))\
            and growth >= 0 else 1

    def show(self):
        """
        Display the plant's name, height, and age in a formatted string.
        The age is displayed in singular or plural form based on its value.
        """
        print(f"{self.name}: {self.height}cm, {self.age_days} "
              f"{'day' if self.age_days == 1 else 'days'} old")

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

    @staticmethod
    def creation(plant_list: list[dict]) -> list["Plant"]:
        """
        Create plants from a list of dict corresponding to plants
        Defined as static method to be called without an instance of the class.
        Args:
        plant_list (list[dict]): a list of dictionaries (typed as list[dict])
        Invalid and missing values are handled by the Plant class constructor.
        Returns:
        _type_: list of Plant objects
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


plants = Plant.creation([
    {'name': 'rose', 'height': 10, 'age': 1},
    {'name': 'Lila', 'age': 9},
    {'name': 'Aloe', 'height': 4.5},
    {'name': 'boolly', 'height': False, 'age': True},
    {'height': 3, 'age': 2},
    {'name': 'Cactus', 'growth': 0.5},
    {'name': 'Sunflower', 'height': 150, 'age': 10, 'growth': 2},
    {'name': 'Kiwi', 'height': 2, 'age': 4, 'growth': 0}
    ])
print("\n=== Plant Factory Output ===")
for plant in plants:
    # end="" suppresses the newline after "Created: "
    # it can be end='/t' to separate with a tab.
    print("Created: ", end='')
    plant.show()
    print(f"Growth rate of {plant.name}: {plant.growth}cm per grow() call")
print(f"\nTotal plants created: {len(plants)}")
days = 3
print(f"\n=== Plant Factory have grown for {days} days ===")
for plant in plants:
    plant.age(days)
    plant.show()
print("\n=== Testing dictionary input ===")
garden: list[dict] = [
    {'name': 'rose', 'height': 10, 'age': 1},
    {'name': 'Lila', 'age': 9},
    {'name': 'Aloe', 'height': 4.5},
    {'name': 'boolly', 'height': False, 'age': True},
    {'height': 3, 'age': 2},
    {'name': 'Cactus', 'growth': 0.5},
    {'name': 'Sunflower', 'height': 150, 'age': 10, 'growth': 2},
    {'name': 'Kiwi', 'height': 2, 'age': 4, 'growth': 0}
    ]
new_plants = Plant.creation(garden)
print("\n=== New Plants Created from Dictionary ===")
print("It must be the same as the previous output")
for plant in new_plants:
    print("Created: ", end='')
    plant.show()
    print(f"Growth rate of {plant.name}: {plant.growth}cm per grow() call")
print(f"\nTotal plants created: {len(new_plants)}")
print(f"\n=== Plant Factory have grown for {days} days ===")
for plant in new_plants:
    plant.age(days)
    plant.show()
