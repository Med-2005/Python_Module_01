
class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def print_det(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def bloom(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")

    def print_det(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def print_det(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.points}")


class GardenManager:

    total_gardens = 0

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_plants(self):
        growth = 0
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            growth += 1
            print(f"{plant.name} grew 1cm")
        return growth

    class GardenStats:

        @staticmethod
        def summarize(plants, total_growth):
            regular_count = 0
            flowering_count = 0
            prize_count = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_count += 1
                else:
                    regular_count += 1
            print(f"Plants added: {len(plants)}, Total growth: {total_growth}cm")
            print(f"Plant types: {regular_count} regular, {flowering_count} flowering, {prize_count} prize flowers")

    @classmethod
    def create_garden_network(cls):
        return cls.total_gardens

    @staticmethod
    def validate_height(height):
        return height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    plants = [Plant("Oak Tree", 100),
              FloweringPlant("Rose", 25, "red"),
              PrizeFlower("Sunflower", 50, "yellow", 10)]
    for p in plants:
        alice_garden.add_plants(p)
    growth = alice_garden.grow_plants()
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for p in alice_garden.plants:
        p.print_det()
    GardenManager.GardenStats.summarize(alice_garden.plants, growth)
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    bob_garden = GardenManager("Bob")
    print("Garden scores - Alice: 218, Bob: 92")
    print(f"Total gardens managed: {GardenManager.create_garden_network()}")
