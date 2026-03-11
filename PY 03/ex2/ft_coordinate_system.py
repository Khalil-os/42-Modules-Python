import math


def distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(text: str) -> tuple:
    parts = text.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    d = distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {d:.2f}\n")
    coord_text = "3,4,0"
    print(f'Parsing coordinates: "{coord_text}"')

    try:
        parsed = parse_coordinates(coord_text)
        print(f"Parsed position: {parsed}")

        d2 = distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {d2}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')

    try:
        parse_coordinates(invalid)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
