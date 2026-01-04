
class Plant:

    total_plants = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total_plants += 1

    def print_det(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":

    Rose = Plant("Rose", 25, 30)
    Oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)

    Rose.print_det()
    Oak.print_det()
    Cactus.print_det()
    Sunflower.print_det()
    Fern.print_det()
    print("\n")
    print(f"Total plants created: {Plant.total_plants}")
