
class Plant:
    # A general class to represent any plant in the garden.

    def __init__(self, name: str, age: int, height: int):
        # Set the name, age, and height for a new plant.
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    # A type of plant that has a color and can bloom.

    def __init__(self, name: str, age: int, height: int, color: str):
        # Create a flower and use the Plant class to set basic info.
        super().__init__(name, age, height)
        self.color = color

    def bloom(self) -> None:
        # Print a message saying the flower is blooming.
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    # A type of plant that has a trunk and provides shade.
    def __init__(self, name: str, age: int, height: int, trunk_diametre: int):
        # Create a tree and use the Plant class to set basic info.
        super().__init__(name, age, height)
        self.trunk_diametre = trunk_diametre

    def produce_shade(self) -> None:
        # Calculate and print how much shade the tree gives.
        shade_area = self.trunk_diametre * 1.56
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    # A type of plant grown for food with nutritional value.
    def __init__(self, name: str, age: int, height: int,
                 harvest_season: str, nutritional_value: str):
        # Create a vegetable and use the Plant class to set basic info.
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_details(self) -> None:
        # Print what vitamins or nutrients the vegetable has.
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
rose = Flower("Rose", 30, 25, "red")
tulip = Flower("Tulip", 20, 15, "yellow")
oak = Tree("Oak", 1825, 500, 50)
pine = Tree("Pine", 1000, 300, 40)
tomato = Vegetable("Tomato", 90, 80, "summer", "vitamin C")
carrot = Vegetable("Carrot", 70, 60, "spring", "vitamin A")

print(
    f"{rose.name} (Flower): {rose.height}, {rose.age} days, {rose.color} color"
)
rose.bloom()
print(
    f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
    f"{oak.trunk_diametre}cm diametre"
)
oak.produce_shade()
print(
    f"{tomato.name}, (Vegetable): {tomato.height}cm, "
    f"{tomato.age}, {tomato.harvest_season} harvest"
)
tomato.print_details()
