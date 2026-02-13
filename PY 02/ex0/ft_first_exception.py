def check_temperature(temp_str: str = None) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        if temp_str is None:
            raise ValueError("No Temperature Input Provided")

        num = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return

    if num >= 0 and num <= 40:
        print(f"Temperature {num}°C is perfect for plants!")
    elif num < 0:
        print(f"Error: {num}°C is too cold for plants (min 0°C)")
    else:
        print(f"Error: {num}°C is too hot for plants (max 40°C)")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
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
