def ft_harvest_total():
    """
    This function asks for the weight of each harvest
    on day 1, day 2, and day 3 and calculates the total.
    Weights are expected to be integers.
    The function prints the total weight.
    """
    total_weight = 0
    for day in range(1, 4):
        weight = int(input(f"Day {day} harvest: "))
        total_weight += weight
    print(total_weight)
