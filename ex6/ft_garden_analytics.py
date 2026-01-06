
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def print_det(self):
        print(f"{self.name} {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def bloom(self):
        print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def print_pr(self):
        print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.points}")


class GardenManager:

    total_gardens = 0

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def grow_plants(self):
        growth = 0
        for plant in self.plants:
            plant.height += 1
            growth += 1
            print(f"{plant.name} grew 1cm")
        return growth

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

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
        if height > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("\n")
    Oak = Plant("Oak Tree", 100)
    Rose = FloweringPlant("Rose", 25, "red")
    Sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    X = [Oak, Rose, Sunflower]

    alice_garden = GardenManager("Alice")
    alice_garden.add_plants(Oak)
    alice_garden.add_plants(Rose)
    alice_garden.add_plants(Sunflower)
    print("\n")
    print("Alice is helping all plants grow...")
    total_growth = alice_garden.grow_plants()
    print("\n")
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    Oak.print_det()
    Rose.bloom()
    Sunflower.print_pr()
    print("\n")
    GardenManager.GardenStats.summarize(X, total_growth)
    print("\n")
    print(f"Height validation test: {GardenManager.validate_height(80)}")
    print("Total gardens managed: ", alice_garden.create_garden_network())
