def ft_plant_age():
    """
    The function asks for a plant age in days and tells you
    whether it is ready to harvest (strictly more than 60 days) or not.
    """
    age = int(input("Enter the plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
