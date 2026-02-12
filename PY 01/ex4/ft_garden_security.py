class SecurePlant:
    """Represents a plant with protected and validated data."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a secure plant."""
        self.name = name
        self.__height = None
        self.__age = None
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Safely update the plant height."""
        if height < 0:
            print("Invalid operation attempted: "
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            if self.__height is not None:
                print(f"Height updated: {height}cm [OK]")
            self.__height = height

    def get_height(self) -> int:
        """Return the plant height."""
        return self.__height

    def set_age(self, age: int) -> None:
        """Safely update the plant age."""
        if age < 0:
            print("Invalid operation attempted: "
                  f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            if self.__age is not None:
                print(f"Age updated: {age} days [OK]")
            self.__age = age

    def get_age(self) -> int:
        """Return the plant age."""
        return self.__age

    def get_info(self) -> None:
        """Display current plant information."""
        if self.__age is None or self.__height is None:
            return
        print(f"\nCurrent plant: {self.name} "
              f"({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    p = SecurePlant("Rose", 15, 56)
    p.set_height(25)
    p.set_age(30)
    p.set_height(-5)
    p.get_info()
