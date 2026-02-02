class SecurePlant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self._height = None
        self._age = None
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Invalid operation attempted: "
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            if self._height is not None:
                print(f"Height updated: {height}cm [OK]")
            self._height = height

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Invalid operation attempted: "
                  f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            if self._age is not None:
                print(f"Age updated: {age} days [OK]")
            self._age = age

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        if self._age is None or self._height is None:
            pass
        else:
            print(f"\nCurrent plant: {self.name} "
                  f"({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    p = SecurePlant("Rose", 15, 56)
    p.set_height(25)
    p.set_age(30)
    p.set_height(-5)
    p.get_info()
