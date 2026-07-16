#!/usr/bin/env python3

def ft_garden_intro():
    """
    This function displays information about a
     plant in the garden..
    """
    print("=== Welcome to My Garden === ")
    plant = "Rose"
    height = 25
    age = 30
    print(f"{plant.capitalize()} in the garden.")
    print(f"Height: {height} cm")
    print(f"Age: {age} days")
    print("=== End of Program === ")


def main():
    ft_garden_intro()


if __name__ == "__main__":
    main()
