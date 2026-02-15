class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


class GardenManager:
    """Manages plants, watering operations, and plant health in the garden."""

    def __init__(self) -> None:
        """Initialize the garden with an empty plant list and a water tank."""
        self.plants = []
        self.water_in_tank = 10

    def add_plant(self, name: str) -> None:
        """Add a plant to the garden after validating its name."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants += [name]
        print(f"Added {name} successfully")

    def water_level(self) -> None:
        """Check whether there is enough water available in the tank."""
        if self.water_in_tank <= 0:
            raise WaterError("Not enough water in the tank")
        else:
            print("There is enough water in the tank")

    def water_plants(self) -> None:
        """Water all plants and always close the watering system."""
        print("Opening watering system")
        try:
            if self.water_in_tank <= 0:
                raise WaterError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant} - success")
                self.water_in_tank -= 1
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water: int, sun: int) -> None:
        """Validate and display the health status of a plant."""
        if name not in self.plants:
            raise PlantError(f"{name} is not in the garden")

        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")

        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """Test the garden management system with valid and invalid scenarios."""
    print("=== Garden Management System ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Error watering plants: {e}")

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 6)
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_in_tank = 0
        manager.water_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(e)
