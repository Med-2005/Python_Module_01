
class Plant:

    # class_attribute

    total_plants = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1

    def print_det(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
        ]
    for p in plants:
        p.print_det()
    print(f"\nTotal plants created: {Plant.total_plants}")
