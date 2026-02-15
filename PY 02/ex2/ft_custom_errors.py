class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


def check_plant_health(name: str, health: int) -> None:
    """Check plant health and raise an error if the plant is unhealthy."""
    if health < 30:
        raise PlantError(f"The {name} plant is wilting!")


def check_water_level(liters: int) -> None:
    """Check water level and raise an error if there is not enough water."""
    if liters <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Test custom garden errors and demonstrate error handling."""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant_health("tomato", 20)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_level(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for health, water in [(20, 10), (80, 0)]:
        try:
            check_plant_health("tomato", health)
            check_water_level(water)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_custom_errors()
    except Exception as e:
        print(e)
