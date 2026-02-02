class Plant:
    type_name = "plant"

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    type_name = "flowering"

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} "
              "flowers (blooming)")


class PrizeFlower(FloweringPlant):
    type_name = "prizeflower"

    def __init__(self, name: str, height: int, color: str, point: int) -> None:
        super().__init__(name, height, color)
        self.point = point

    def print_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming), Prize points: {self.point}")


class GardenManager:
    def __init__(self) -> None:
        self.gardens = {}

    def add_garden(self, name: str) -> None:
        self.gardens[name] = []

    def add_plant(self, name: str, plant: Plant) -> None:
        if name not in self.gardens:
            self.add_garden(name)
        self.gardens[name] += [plant]
        print(f"Added {plant.name} to {name}'s garden")

    def grow_all(self, name: str) -> None:
        if name not in self.gardens:
            return
        for i in self.gardens[name]:
            i.height += 1
        print(f"{name} is helping all plants grow...")
        for i in self.gardens[name]:
            print(f"{i.name} grew 1cm")

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def count_plants(self) -> int:
            count: int = 0
            for i in self.plants:
                count += 1
            return count

        def total_height(self) -> int:
            count: int = 0
            for i in self.plants:
                count += i.height
            return count

        def count_types(self) -> int:
            counts: dict = {
                "plant": 0,
                "flowering": 0,
                "prizeflower": 0
            }
            for i in self.plants:
                counts[i.type_name] += 1
            return counts

    def calculate_score(self, name: str) -> int:
        if name not in self.gardens:
            return 0
        total_score = 0
        for i in self.gardens[name]:
            total_score += i.height
            if i.type_name == "prizeflower":
                total_score += i.point
        return total_score

    def create_garden_network(cls, managers: list) -> None:
        result = ""
        index = 0
        count = 0
        for _ in managers:
            count += 1
        for m in managers:
            for garden_name in m.gardens:
                score = m.calculate_score(garden_name)
                result += f"{garden_name}: {score}"
                break
            if index < count - 1:
                result += ", "
            index += 1
        print(f"Garden scores - {result}")
        print(f"Total gardens managed: {count}")
    create_garden_network = classmethod(create_garden_network)

    def is_valid_height(height: int) -> bool:
        return height >= 0
    is_valid_height = staticmethod(is_valid_height)

    def print_report(self, name: str) -> None:
        if name not in self.gardens:
            return
        print(f"=== {name}'s Garden Report ===", "\nPlants in garden:")
        for i in self.gardens[name]:
            i.print_info()

    def print_summary(self, name: str, growth: int) -> None:
        if name not in self.gardens:
            return

        plants = self.gardens[name]
        stats = GardenManager.GardenStats(plants)

        total_plants = stats.count_plants()
        types = stats.count_types()

        print(f"Plants added: {total_plants}, Total growth: {growth}cm")
        print(f"Plant types: {types['plant']} regular, {types['flowering']} "
              f"flowering, {types['prizeflower']} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()

    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", FloweringPlant("Rose", 25, "red"))
    manager.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    before = GardenManager.GardenStats(manager.gardens["Alice"]).total_height()
    manager.grow_all("Alice")
    after = GardenManager.GardenStats(manager.gardens["Alice"]).total_height()
    growth = after - before
    print()
    manager.print_report("Alice")
    print()
    manager.print_summary("Alice", growth)

    print("\nHeight validation test:", GardenManager.is_valid_height(10))
    print()

    manager2 = GardenManager()
    manager2.add_plant("Bob", Plant("Pine", 90))
    manager2.add_plant("Bob", Plant("Cedar", 2))
    print()

    GardenManager.create_garden_network([manager, manager2])
