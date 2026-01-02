
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def plant_age(self):
        self.age += 1

    def plant_height(self):
        self.height += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())

    start_height = rose.height

    for i in range(6):
        rose.plant_age()
        rose.plant_height()

    print("=== Day 7 ===")
    print(rose.get_info())

    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
