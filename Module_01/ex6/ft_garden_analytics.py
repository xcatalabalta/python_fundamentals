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

    @staticmethod
    def more_than_a_year_old(days):
        """
        Check if the plant is more than a year old.
        Args:
            days (int): The age of the plant in days.
        Returns:
            bool: True if the plant is more than a year old, False otherwise.
        """
        return days > 365


class Flower(Plant):
    """
    A class to represent a flower in the garden.
    Inherits from the Plant class.
    Additional attributes: color, bloomed.
    Bloomed is a boolean indicating whether the flower has bloomed or not.
    Bloomed is initialized to False by default.
    """
    def __init__(self, name="flower", height=0, age=0, growth=1, color="??"):
        """
        Initialize a Flower instance.
        Inherits from the Plant class and adds a color attribute.
        Initializes bloomed status to False
        Args:
            name (str): The name of the flower.
            height (int/float): The height of the flower.
            age (int/float): The age of the flower.
            growth (int/float): The growth rate of the flower.
            color (str): The color of the flower.
        Returns:
            _type_: None
        """
        super().__init__(name, height, age, growth)
        self._color = color if isinstance(color, str) else "??"
        self._bloomed = False

    def set_color(self, new_color):
        """
        Set the color of the flower to a new value.
        The new color must be a string.
        Otherwise, the color remains unchanged.
        Args:
            new_color (str): The new color value.
        Returns:
            _type_: None
        """
        if isinstance(new_color, str):
            self._color = new_color
            print(f"Color updated: {self._color}")
        else:
            print(f"{self.name}: Error, color must be a string.")
            print("Update rejected.")

    def set_bloomed(self, bloomed):
        """
        Set the bloomed status of the flower.
        The bloomed status must be a boolean value.
        Otherwise, the bloomed status remains unchanged.
        Args:
            bloomed (bool): The new bloomed status.
        Returns:
            _type_: None
        """
        if isinstance(bloomed, bool):
            self._bloomed = bloomed
            print(f"Bloomed status updated: {self._bloomed}")
        else:
            print(f"{self.name}: Error, bloomed status must be a boolean.")
            print("Update rejected.")

    def get_color(self):
        """
        Get the current color of the flower.
        Returns:
            _type_: str
        """
        return self._color

    def bloom(self):
        """
        Set the flower's bloomed status to True.
        Returns:
            _type_: None
        """
        self._bloomed = True

    def show(self):
        """
        Display the flower's attributes in a formatted string.
        Use the show method from the Plant class
        Add color and bloomed status.
        Returns:
            _type_: None
        """
        super().show()
        print(f" Color: {self._color}")
        status = ("is blooming beautifully!" if self._bloomed
                  else " has not bloomed yet")
        print(f" {self.name} {status}")


class Tree(Plant):
    """
    A class to represent a tree in the garden.
    Inherits from the Plant class.
    Additional attributes: trunk_diameter.
    Additional ability: produce_shade()
    """
    def __init__(self, name="tree", height=0, age=0, growth=10):
        """
        Initialize a Tree instance.
        Inherits from the Plant class
        Leaves trunk_diameter attribute to be added later.
        Args:
            name (str): The name of the tree.
            height (int/float): The height of the tree.
            age (int/float): The age of the tree.
            growth (int/float): The growth rate of the tree.
        Returns:
            _type_: None
        """
        super().__init__(name, height, age, growth)

    def set_trunk_diameter(self, new_diameter):
        """
        Set the trunk diameter of the tree to a new value.
        The new diameter must be a positive number.
        Otherwise, the diameter remains unchanged.
        Args:
            new_diameter (int/float): The new trunk diameter value.
        Returns:
            _type_: None
        """
        if isinstance(new_diameter, (int, float)) and new_diameter >= 0:
            self._trunk_diameter = new_diameter
            print(f"Trunk diameter updated: {self._trunk_diameter}cm")
        elif isinstance(new_diameter, (int, float)) and new_diameter < 0:
            print(f"{self.name}: Error, trunk diameter cannot be negative.")
            print("Update rejected.")
        else:
            print(f"{self.name}: Error, trunk diameter must be a number.")
            print("Update rejected.")

    def get_trunk_diameter(self):
        """
        Get the current trunk diameter of the tree.
        Returns:
            _type_: float
        """
        try:
            return self._trunk_diameter
        except AttributeError:
            return None

    def produce_shade(self):
        """
        Simulate the tree producing shade.
        Returns:
            _type_: None
        """
        try:
            diameter = self._trunk_diameter
        except AttributeError:
            print(f"{self.name}: No diameter, no shade.")
            return
        if self._height > 0 and diameter > 0:
            print(f"Tree {self.name} now produces a shade of "
                  f"{self._height}cm long and {diameter}cm wide.")
        else:
            print(f"Tree {self.name} is too short to produce shade.")

    def grow(self, growth=None):
        """
        Increase the height of the tree by the specified growth amount.
        The growth amount must be a positive number.
        Otherwise, the height remains unchanged.
        If growth is None, the tree grows by its default growth rate.
        Args:
            growth (int/float): The amount by which the tree should grow.
        Returns:
            _type_: None
        """
        super().grow(growth)
        try:
            diameter = self._trunk_diameter
        except AttributeError:
            diameter = 0
        self._trunk_diameter = diameter
        if isinstance(growth, (int, float)) and growth > 0:
            self._trunk_diameter += growth / 10
        else:
            self._trunk_diameter += self._growth / 10

    def show(self):
        """
        Display the tree's attributes in a formatted string.
        Use the show method from the Plant class
        Add trunk diameter.
        Returns:
            _type_: None
        """
        super().show()
        diameter = self.get_trunk_diameter()
        if diameter is not None:
            print(f" Trunk diameter: {diameter}cm")
        else:
            print(" Trunk diameter: Not set")


class Vegetable(Plant):
    """
    A class to represent a vegetable in the garden.
    Inherits from the Plant class.
    Additional attributes:
    - harvest_season
    - nutritional_value.
    """
    def __init__(self, name="vegetable", height=0, age=0, growth=1):
        """
        Initialize a Vegetable instance.
        Inherits from the Plant class
        Initializes harvest_season and nutritional_value attributes.
        Args:
            name (str): The name of the vegetable.
            height (int/float): The height of the vegetable.
            age (int/float): The age of the vegetable.
            growth (int/float): The growth rate of the vegetable.
        Returns:
            _type_: None
        """
        super().__init__(name, height, age, growth)
        self._harvest_season = None
        self._nutritional_value = 0

    def set_harvest_season(self, season):
        """
        Set the harvest season of the vegetable.
        The season must be a string.
        Otherwise, the harvest season remains unchanged.
        Args:
            season (str): The new harvest season value.
        Returns:
            _type_: None
        """
        seasons = ['summer', 'winter', 'autumn', 'spring']
        if isinstance(season, str) and season in seasons:
            self._harvest_season = season
        else:
            print(f"{self.name}: Error. Please provide a valid season:")
            # commented out because it was not authorized by the instructions.
            # print(f"Valid seasons are: {', '.join(seasons)}.")
            print(seasons)

    def set_nutritional_value(self, value):
        """
        Set the nutritional value of the vegetable.
        The value must be a positive number.
        Otherwise, the nutritional value remains unchanged.
        Args:
            value (int/float): The new nutritional value.
        Returns:
            _type_: None
        """
        if isinstance(value, (int, float)) and value > 0:
            self._nutritional_value = value
        else:
            print(f"{self.name}: Error. Please provide a positive number.")

    def get_harvest_season(self):
        """
        Get the current harvest season of the vegetable.
        Returns:
            _type_: str
        """
        return self._harvest_season

    def get_nutritional_value(self):
        """
        Get the current nutritional value of the vegetable.
        Returns:
            _type_: float
        """
        return self._nutritional_value

    def grow(self, growth=None):
        """
        Increase the height of the vegetable by the specified growth amount.
        The growth amount must be a positive number.
        Otherwise, the height remains unchanged.
        If growth is None, the vegetable grows by its default growth rate.
        Increase the nutritional value by 10% of the growth amount.
        If growth is None, the value increases by 10% of the default rate.
        Args:
            growth (int/float): The amount by which the vegetable should grow.
        Returns:
            _type_: None
        """
        super().grow(growth)
        if isinstance(growth, (int, float)) and growth > 0:
            self._nutritional_value += growth * 0.1
        else:
            self._nutritional_value += self._growth * 0.1

    def show(self):
        """
        Display the vegetable's attributes in a formatted string.
        Use the show method from the Plant class
        Add harvest season and nutritional value.
        Nutritional value is displayed with three decimal places.
        (Probaly not allowed by the instructions)
        (Just to learn how to format floats in f-strings)
        Returns:
            _type_: None
        """
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {self.get_nutritional_value():.3f}")


rose = Flower("Rose", 15, 10, 2, "red")
oak = Tree("Oak", 100, 565, 10)
tomato = Vegetable("Tomato", 30, 200, 3)
print("=== Garden statistics ===")
print("Our garden has the following plants:")
rose.show()
oak.show()
tomato.show()
print("=== Check year-old plants ===")
garden_plants = [rose, oak, tomato]
for plant in garden_plants:
    plant.show()
    word = "is" if plant.more_than_a_year_old(plant.get_age()) else \
        "\033[91mis not\033[0m"
    print(f"{plant.name} {word} more than a year old.")
for x in range(30, 400, 90):
    print(f"Is {x} days more than a year? -> {rose.more_than_a_year_old(x)}")
    for plant in garden_plants:
        plant.age(30)
        plant.show()
