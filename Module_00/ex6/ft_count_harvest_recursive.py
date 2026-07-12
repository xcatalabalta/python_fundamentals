def ft_count_harvest_recursive():
    """
    The function asks for the number of days until harvest.
    It prints each day until that number is reached, using recursion.
    """
    days_until_harvest = int(input("Enter the number of days until harvest: "))
    
    def print_days(day):
        if day > days_until_harvest:
            return
        print(f"Day {day}")
        print_days(day + 1)
    
    print_days(1)
    print("Harvest time!")
