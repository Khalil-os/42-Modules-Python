class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self._age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self._age} days old"


if __name__ == "__main__":
    p = Plant("Rose", 25, 30)

    start_height = p.height

    print("=== Day 1 ===")
    print(p.get_info())

    days_simulate = 6

    for i in range(days_simulate):
        p.grow()
        p.age()

    print(f"=== Day {days_simulate + 1} ===")
    print(p.get_info())

    print(f"Growth this week: +{days_simulate}cm")
