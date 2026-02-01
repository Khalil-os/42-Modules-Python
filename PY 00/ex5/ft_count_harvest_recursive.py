def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def counter(day: int) -> None:
        if day > days:
            return
        print(f"Day {day}")
        day += 1
        counter(day)

    counter(1)
    print("Harvest time!")
