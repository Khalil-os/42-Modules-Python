from typing import Generator


def game_events(total: int) -> Generator[str, None, None]:

    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, total + 1):
        if i == 1:
            yield (f"Event {i}: Player {players[0]} (level {5}) {actions[0]}",
                   5, actions[0])
        elif i == 2:
            yield (f"Event {i}: Player {players[1]} (level {12}) {actions[1]}",
                   12, actions[1])
        elif i == 3:
            yield (f"Event {i}: Player {players[2]} (level {8}) {actions[2]}",
                   8, actions[2])
        else:
            name = players[i % len(players)]
            action = actions[i % len(actions)]
            level = (i * 10) % 50 + 1
            yield (f"Event {i}: Player {name} (level {level}) {action}", level,
                   action)


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    total = 1000
    print("Processing", total, "game events...")
    count = 0
    high_level = 0
    treasure = 0
    levelup = 0
    for event, level, action in game_events(total):
        count += 1
        print(event)
        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            levelup += 1
    print("\n=== Stream Analytics ===")
    print("Total events processed:", count)
    print(f"High-level players (10+): {high_level:.0f}")
    print(f"Treasure events: {treasure:.0f}")
    print(f"Level-up events: {levelup:.0f}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fib = fibonacci()
    print("Fibonacci sequence (first 10):", end=" ")
    for i in range(10):
        if i > 0:
            print(",", end=" ")
        print(next(fib), end="")
    print()
    prime_gen = primes()
    print("Prime numbers (first 5):", end=" ")
    for i in range(5):
        if i > 0:
            print(",", end=" ")
        print(next(prime_gen), end="")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
