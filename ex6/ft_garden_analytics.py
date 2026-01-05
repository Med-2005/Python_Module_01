
class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:

    total_gardens = 0

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plants(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")


my_garden = GardenManager("Mohamed")
rose = Plant("Rose", 25)
my_garden.add_plants(rose)
print(GardenManager.total_gardens)
