"""
This program models a Plant that can grow over time.
It simulates daily aging and height growth.
"""


class Plant:
    """
    Blueprint for a Plant with growth actions.

    Attributes:
        name (str): Name of the plant
        height (int): Height in centimeters
        ag (int): Age in days
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a new Plant object.

        Args:
            name (str): Plant name
            height (int): Initial height in cm
            age (int): Initial age in days
        """
        self.name = name
        self.height = height
        self.ag = age

    def age(self):
        """
        Increases the plant's age by one day.
        """
        self.ag += 1

    def grow(self):
        """
        Increases the plant's height by one centimeter.
        """
        self.height += 1

    def get_info(self):
        """
        Returns a formatted string describing the plant.
        """
        return f"{self.name}: {self.height}cm, {self.ag} days old"


"""
Program entry point.
Creates a Plant instance and simulates its growth over several days.
"""
if __name__ == "__main__":

    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    start_height = rose.height

    for i in range(6):
        rose.age()
        rose.grow()

    print("=== Day 7 ===")
    print(rose.get_info())

    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
