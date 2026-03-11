def garden_operations(error_type: str) -> None:
    """Raise different built-in errors based on the given type."""
    if error_type == "value":
        int("abc")

    elif error_type == "zero":
        1 / 0

    elif error_type == "file":
        open("missing.txt")

    elif error_type == "key":
        data = {}
        print(data["missing_plant"])


def test_error_types() -> None:
    """Test handling of different built-in Python errors."""
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(e)
