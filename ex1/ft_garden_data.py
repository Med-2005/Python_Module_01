# Create a blueprint for a Plant object
class Plant:
    # This runs when we create a new plant
    def __init__(self, name, height, age):
        self.name = name      # Set the plant's name
        self.height = height  # Set the plant's height
        self.age = age        # Set the plant's age

    # A function inside the class to print plant details
    def print_det(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


# Main program starts here

if __name__ == "__main__":

    # Store multiple plant objects in a list
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")

    # Loop through each plant in the list
    for p in plants:
        # Call the print function for each plant
        Plant.print_det(p)
