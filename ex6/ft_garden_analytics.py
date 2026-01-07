# The base class (Parent) for all plants
class Plant:
    def __init__(self, name: str, height: int):
        # Store name and height inside the object
        self.name = name
        self.height = height

    # Function to print basic plant details
    def print_det(self):
        print(f"- {self.name}: {self.height}cm")


# A specific type of plant that has flowers (Inherits from Plant)
class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        # Use the parent (Plant) to set name and height
        super().__init__(name, height)
        # Add a new property: flower color
        self.color = color

    # Special action only for flowering plants
    def bloom(self):
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming)")

    # Update (Override) the print function to include color
    def print_det(self):
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming)")


# A special flowering plant that wins prizes (Inherits from FloweringPlant)
class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        # Use FloweringPlant to set name, height, and color
        super().__init__(name, height, color)
        # Add a new property: prize points
        self.points = points

    # Update print function to include prize points
    def print_det(self):
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming), Prize points: {self.points}")


# The main class to manage the garden
class GardenManager:
    # A shared variable to count how many gardens exist in total
    total_gardens = 0

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        # A list to store all plant objects
        self.plants = []
        # Increase the total garden count whenever a new manager is created
        GardenManager.total_gardens += 1

    # Add a plant object to the list
    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    # Increase the height of every plant in the garden by 1
    def grow_plants(self):
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
        # Return how many plants grew
        return len(self.plants)

    # A helper class for showing statistics
    class GardenStats:
        @staticmethod
        def summarize(plants, total_growth):
            # Counters for each type of plant
            regular = flowering = prize = 0
            for p in plants:
                # Check the specific type of each plant using inheritance logic
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            # Print the final report
            print(f"Total plants: {len(plants)}, "
                  f"Total growth: {total_growth}cm")
            print(f"Regular: {regular}, Flowering: "
                  f"{flowering}, Prize: {prize}")

    # A class method to check the shared total_gardens variable
    @classmethod
    def create_garden_network(cls):
        return cls.total_gardens

    # A simple tool to check if a height value is valid (positive)
    @staticmethod
    def validate_height(height):
        return height > 0


# --- Main Program Execution ---
if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # 1. Create a garden for Alice
    alice_garden = GardenManager("Alice")

    # 2. Create different types of plant objects
    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]

    # 3. Add the plants to Alice's garden
    for p in plants:
        alice_garden.add_plants(p)

    # 4. Make them grow
    growth = alice_garden.grow_plants()

    # 5. Show the report
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for p in alice_garden.plants:
        p.print_det()

    # 6. Show stats using the nested class
    GardenManager.GardenStats.summarize(alice_garden.plants, growth)

    # 7. Test utility functions
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    # 8. Create another garden to see the total count increase
    bob_garden = GardenManager("Bob")
    print(f"Total gardens managed: {GardenManager.create_garden_network()}")
