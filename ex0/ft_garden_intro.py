"""
This program displays basic information about a plant
such as its name, height, and age.
"""


def main():
    """
    Main function of the program.

    It sets the plant information and prints it
    in a simple formatted way.
    """
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


"""
This condition ensures that the main function
runs only when the file is executed directly.
"""
if __name__ == "__main__":
    main()
