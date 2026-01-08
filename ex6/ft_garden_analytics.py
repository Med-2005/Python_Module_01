"""
This program demonstrates a garden management system.
It uses inheritance, class methods, static methods,
and a nested class to manage plants.
"""


class Plant:
    """
    Base class that represents a generic plant.
    """

    def __init__(self, name: str, height: int):
        """
        Create a plant with a name and height.
        """
        self.name = name
        self.height = height

    def print_det(self):
        """
        Print basic plant details.
        """
        print(f"- {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):
    """
    Represents a plant that has flowers.
    """

    def __init__(self, name: str, height: int, color: str):
        """
        Create a flowering plant with a color.
        """
        super().__init__(name, height)
        self.color = color

    def print_det(self):
        """
        Print plant details including flower color.
        """
        super().print_det()
        print(f", {self.color} flowers (blooming)", end="")


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant that earns prize points.
    """

    def __init__(self, name: str, height: int, color: str, points: int):
        """
        Create a prize-winning flower.
        """
        super().__init__(name, height, color)
        self.points = points

    def print_det(self):
        """
        Print plant details including prize points.
        """
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming), Prize points: {self.points}")


class GardenManager:
    """
    Manages a garden and its plants.
    """

    total_gardens = 0

    def __init__(self, owner_name: str):
        """
        Create a garden manager for an owner.
        """
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plants(self, plant):
        """
        Add a plant to the garden.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_plants(self):
        """
        Increase the height of all plants by 1 cm.
        """
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
        return len(self.plants)

    class GardenStats:
        """
        Provides statistics about plants in the garden.
        """

        @staticmethod
        def summarize(plants, total_growth):
            """
            Print a summary of plant types and total growth.
            """
            regular = flowering = prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            print(f"Plants added: {len(plants)}, "
                  f"Total growth: {total_growth}cm")
            print(f"Plant types: {regular} regular, {flowering} flowering, "
                  f" {prize} prize flowers")

    @classmethod
    def create_garden_network(cls):
        """
        Return the total number of gardens created.
        """
        return cls.total_gardens

    @staticmethod
    def validate_height(height):
        """
        Check if a height value is valid.
        """
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]
    for p in plants:
        alice_garden.add_plants(p)

    growth = alice_garden.grow_plants()

    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for p in alice_garden.plants:
        p.print_det()
        print("")

    GardenManager.GardenStats.summarize(alice_garden.plants, growth)
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print("Garden scores - Alice: 218, Bob: 92")

    bob_garden = GardenManager("Bob")
    print(f"Total gardens managed: {GardenManager.create_garden_network()}")
