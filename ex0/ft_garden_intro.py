# The main part of our program
def main():
    # Set the information for the plant
    name = "Rose"      # The name of the flower
    height = 25        # How tall it is (cm)
    age = 30           # How old it is (days)

    # Print the start message
    print("=== Welcome to My Garden ===")

    # Show the plant info on the screen
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")

    # Print the finish message
    print("=== End of Program ===")


# This line tells Python to start the program here

if __name__ == "__main__":
    main()
