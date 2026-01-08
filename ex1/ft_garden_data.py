"""
This program demonstrates how to create a Plant class,
store multiple Plant objects in a list, and display
their details.
"""


class Plant:
    """
    A blueprint for creating Plant objects.

    Attributes:
        name (str): The name of the plant
        height (int): The height of the plant in centimeters
        age (int): The age of the plant in days
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a new Plant instance.

        Args:
            name (str): Plant name
            height (int): Plant height in cm
            age (int): Plant age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def print_det(self):
        """
        Prints the details of the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


"""
Entry point of the program.
Creates a list of Plant objects and displays their details.
"""
if __name__ == "__main__":

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")

    for p in plants:
        Plant.print_det(p)
