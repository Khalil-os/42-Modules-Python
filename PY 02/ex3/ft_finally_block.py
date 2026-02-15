def water_plants(plant_list: list) -> None:
    """Water each plant and always close the watering system."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant lists."""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")

    plant_list = [
        "tomato",
        "lettuce",
        "carrots",
    ]
    water_plants(plant_list)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    plants_with_errors = [
        "tomato",
        None,
    ]
    water_plants(plants_with_errors)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(e)
