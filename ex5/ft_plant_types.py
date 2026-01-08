
"""
This program demonstrates different plant types in a garden.
It uses inheritance to model flowers, trees, and vegetables.
"""


class Plant:
    """
    General class to represent any plant in the garden.
    """

    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, age: int, height: int, color: str):
        super().__init__(name, age, height)
        self.color = color

    def print_det(self):
        """
        Overridden to include type and color.
        """
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")

    def bloom(self):
        """
        Show the flower blooming.
        """
        self.print_det()
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, age: int, height: int, trunk_diametre: int):
        super().__init__(name, age, height)
        self.trunk_diametre = trunk_diametre

    def print_det(self):
        """
        Overridden to include type and trunk diameter.
        """
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diametre}cm diameter")

    def produce_shade(self):
        """
        Show the tree shade.
        """
        self.print_det()
        print(f"{self.name} provides "
              f"{self.trunk_diametre} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_det(self):
        """
        Overridden to include type and harvest season.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 30, 25, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")
    oak = Tree("Oak", 1825, 500, 50)
    pine = Tree("Pine", 1000, 300, 40)
    tomato = Vegetable("Tomato", 90, 80, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 70, 60, "spring", "vitamin A")

    rose.bloom()
    oak.produce_shade()
    tomato.print_det()
