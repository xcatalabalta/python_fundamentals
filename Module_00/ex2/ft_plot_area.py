def ft_plot_area():
    """
    This function calculates the area of a rectangular plot of land.

    It prompts the user to input the length and width of the plot,
    then calculates and returns the area.

    It prints the area to the console(length * width).
    """
    # Prompt the user for length and width
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    # Calculate area
    area = length * width

    print(area)
