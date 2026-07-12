def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    This function takes a seed type, quantity, and unit of measurement.
    It prints the inventory information based on the provided parameters.
    """
    seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
