"""
This program demonstrates different plant types in a garden.
It uses inheritance to model flowers, trees, and vegetables.
"""


class Plant:
    """
    General class to represent any plant in the garden.
    """

    def __init__(self, name: str, age: int, height: int):
        """
        Create a plant with a name, age, and height.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flower that can bloom and has a color.
    """

    def __init__(self, name: str, age: int, height: int, color: str):
        """
        Create a flower using the Plant class information.
        """
        super().__init__(name, age, height)
        self.color = color

    def bloom(self) -> None:
        """
        Print a message when the flower blooms.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree that can produce shade.
    """

    def __init__(self, name: str, age: int, height: int, trunk_diametre: int):
        """
        Create a tree with a trunk diameter.
        """
        super().__init__(name, age, height)
        self.trunk_diametre = trunk_diametre

    def produce_shade(self) -> None:
        """
        Calculate and print the shade produced by the tree.
        """

        print(f"{self.name} provides {self.trunk_diametre} "
              f"square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable grown for food.
    """

    def __init__(self, name: str, age: int, height: int,
                 harvest_season: str, nutritional_value: str):
        """
        Create a vegetable with harvest season and nutrition info.
        """
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_details(self) -> None:
        """
        Print the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


"""
Program entry point.
Creates different plant objects and shows their behavior.
"""
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    rose = Flower("Rose", 30, 25, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")
    oak = Tree("Oak", 1825, 500, 50)
    pine = Tree("Pine", 1000, 300, 40)
    tomato = Vegetable("Tomato", 90, 80, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 70, 60, "spring", "vitamin A")

    print(
        f"{rose.name} (Flower): {rose.height}cm, "
        f"{rose.age} days, {rose.color} color")

    rose.bloom()
    print("")
    print(
        f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diametre}cm diametre"
    )
    oak.produce_shade()
    print("")
    print(
        f"{tomato.name} (Vegetable): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harvest_season} harvest"
    )
    tomato.print_details()
