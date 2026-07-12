def ft_count_harvest_iterative():
    """
    The function asks for the number of days until harvest.
    It prints each day until that number is reached.
    """
    days_until_harvest = int(input("Enter the number of days until harvest: "))
    for day in range(1, days_until_harvest + 1):
        print(f"Day {day}")
    print("Harvest time!")
