class Plant:
    """Represents a basic plant with common attributes."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ===")
    for i in plants:
        print(f"{i.name}: {i.height}cm, {i.age} days old")
