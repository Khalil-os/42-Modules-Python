def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        val = "abc"
        int(val)
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        x = 1 / 0
        print(x)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")

    try:
        print("Testing KeyError...")
        x = {}
        print(x["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    try:
        print("\nTesting multiple errors together...")
        val = "abc"
        int(val)
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(e)
