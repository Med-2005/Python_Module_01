
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":

    rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age}days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age}days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age}days old")
