def ft_water_reminder():
    """
    This function asks for the number of days since the
    last watering. If it has been more than 2 days, print "Water the plants!";
    otherwise print "Plants are fine".
    """
    days_since_watering = int(input("Days since last watering: "))
    if days_since_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
