class Plant:
    """Represents a basic plant with common attributes."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name = name
        self.height = height
        self.age = age


def length() -> int:
    """Count the number of plants."""
    count: int = 0
    for i in plants:
        count += 1
    return count


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in plants:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")
    print(f"\nTotal plants created: {length()}")
