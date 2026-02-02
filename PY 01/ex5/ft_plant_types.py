class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age,
                 harvest_season, nutritional_value) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer", "C")

    print("=== Garden Plant Types ===")
    print(f"\n{flower.name} (Flower): {flower.height}cm, "
          f"{flower.age} days, {flower.color} color")
    flower.bloom()

    print(f"\n{tree.name} (Tree): {tree.height}cm, "
          f"{tree.age} days, {tree.trunk_diameter}cm diameter")
    tree.produce_shade()

    print(f"\n{vegetable.name} (Vegetable): {vegetable.height}cm, "
          f"{vegetable.age} days, {vegetable.harvest_season} harvest")
    vegetable.info()
