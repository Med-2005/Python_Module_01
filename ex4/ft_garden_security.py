"""
This program demonstrates a secure plant class.
It protects plant data using encapsulation and validation.
"""


class SecurePlant:
    """
    A plant class that protects data integrity
    by controlling access to its attributes.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Create a SecurePlant object with validated data.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """
        Return the plant height safely.
        """
        return self.__height

    def set_height(self, height: int):
        """
        Set the plant height if the value is valid.
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_age(self) -> int:
        """
        Return the plant age safely.
        """
        return self.__age

    def set_age(self, age: int):
        """
        Set the plant age if the value is valid.
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def print_info(self):
        """
        Print the current plant information.
        """
        print(
            f"Current plant: {self.__name}"
            f" ({self.__height}cm, {self.__age} days)"
        )


"""
Program entry point.
Tests the SecurePlant class behavior.
"""
if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print("\n")
    rose.set_height(-5)
    print("\n")
    rose.print_info()
