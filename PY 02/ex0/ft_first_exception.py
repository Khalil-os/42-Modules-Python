def check_temperature(temp_str: str = None) -> None:
    """Validate whether a temperature value is suitable for plants."""
    print(f"Testing temperature: {temp_str}")
    try:
        if temp_str is None:
            raise ValueError("No Temperature Input Provided")
        try:
            temp = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number")
            return
        if temp > 40:
            raise ValueError(f"Error: {temp}°C is too hot "
                             "for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"Error: {temp}°C is too cold "
                             "for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")

    except ValueError as e:
        print(e)


def test_temperature_input() -> None:
    """Test temperature validation with valid and invalid inputs."""
    print("=== Garden Temperature Checker ===\n")

    check_temperature("25.5")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
