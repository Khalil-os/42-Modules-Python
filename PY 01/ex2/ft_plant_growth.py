class Plant:
    """Represents a basic plant with common attributes."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        """Increase the plant height by one unit."""
        self.height += 1

    def age(self) -> None:
        """Increase the plant age by one day."""
        self._age += 1

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name}: {self.height}cm, {self._age} days old"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
    ]

    print("=== Day 1 ===")
    for p in plants:
        print(p.get_info())

    days_simulate = 6

    for _ in range(days_simulate):
        for p in plants:
            p.grow()
            p.age()

    print(f"\n=== Day {days_simulate + 1} ===")
    for p in plants:
        print(p.get_info())
    print(f"Growth this week: +{days_simulate}cm")
