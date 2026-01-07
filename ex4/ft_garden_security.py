
class SecurePlant:
    """A plant class that protects data integrity through encapsulation."""

    def __init__(self, name: str, height: int, age: int):
        """Initializes a SecurePlant instance."""
        self.__name = name
        """We initialize with a default value and use setters to validate"""
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Safe way to access plant height data."""
        return self.__height

    def set_height(self, height: int):
        """Controlled way to modify height with validation."""
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_age(self) -> int:
        """Safe way to access plant age data"""
        return self.__age

    def set_age(self, age: int):
        """Controlled way to modify age with validation."""
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def print_info(self):
        """Print the current state of the plant."""
        print(
            f"Current plant: {self.__name}"
            f" ({self.__height}cm, {self.__age} days)"
        )





ob = SecurePlant("loi", -23, -453)


ob.print_info()






# if __name__ == "__main__":
#     print("=== Garden Security System ===")
#     rose = SecurePlant("Rose", -25, 30)
#     rose.__height = 5
#     print(rose.__height)
#     # rose.set_height(-5)

#     # rose.print_info()
