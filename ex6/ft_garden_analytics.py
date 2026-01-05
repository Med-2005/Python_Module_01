
class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def bloom(self):
        pass


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
