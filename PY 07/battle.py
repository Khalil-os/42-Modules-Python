from __future__ import annotations

from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(
    factory_one: CreatureFactory,
    factory_two: CreatureFactory
) -> None:
    creature_one = factory_one.create_base()
    creature_two = factory_two.create_base()

    print(creature_one.describe())
    print(" vs.")
    print(creature_two.describe())
    print(" Fight!")

    print(creature_one.attack())
    print(creature_two.attack())


def main() -> None:
    fire = FlameFactory()
    water = AquaFactory()

    print("Testing factory")
    test_factory(fire)

    print()
    print("Testing factory")
    test_factory(water)

    print()
    print("Testing battle")
    battle(fire, water)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
