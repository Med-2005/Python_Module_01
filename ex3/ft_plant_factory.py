"""
This program demonstrates the use of a class attribute
to count how many Plant objects are created.
"""


class Plant:
    """
    Represents a plant and keeps track of the total number
    of Plant instances created.

    Class Attributes:
        total_plants (int): Counts all created Plant objects
    """

    total_plants = 0

    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Name of the plant
            height (int): Height of the plant in centimeters
            age (int): Age of the plant in days
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1

    def print_det(self):
        """
        Prints the creation details of the plant.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


"""
Program entry point.
Creates several Plant objects and displays their details,
then prints the total number of created plants.
"""
if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    for p in plants:
        p.print_det()

    print(f"\nTotal plants created: {Plant.total_plants}")
