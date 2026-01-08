# Blueprint for a plant with growth actions
class Plant:
    def __init__(self, name, height, age):
        self.name = name      # Name of the plant
        self.height = height  # Height in cm
        self.age = age        # Age in days

    # Method to increase age by 1
    def plant_age(self):
        self.age += 1

    # Method to increase height by 1
    def plant_height(self):
        self.height += 1

    # Method to return formatted info string
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    # Create an instance (Object)
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    # Save the initial height to calculate growth later
    start_height = rose.height

    # Simulate growth over 6 days (to reach Day 7)
    for i in range(6):
        rose.plant_age()
        rose.plant_height()

    print("=== Day 7 ===")
    print(rose.get_info())

    # Calculation showing state change
    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")
