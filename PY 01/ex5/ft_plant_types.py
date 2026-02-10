class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1500, 40),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "C"),
        Vegetable("Carrot", 40, 70, "winter", "A"),
    ]

    print("=== Garden Plant Types ===")
    for flower in flowers:
        print(f"\n{flower.name} (Flower): {flower.height}cm, "
              f"{flower.age} days, {flower.color} color")
        flower.bloom()

    for tree in trees:
        print(f"\n{tree.name} (Tree): {tree.height}cm, "
              f"{tree.age} days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade()

    for vegetable in vegetables:
        print(f"\n{vegetable.name} (Vegetable): {vegetable.height}cm, "
              f"{vegetable.age} days, {vegetable.harvest_season} harvest")
        vegetable.info()
