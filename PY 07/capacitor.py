from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def main() -> None:
    heal_factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")

    base = heal_factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = heal_factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    transform_factory = TransformCreatureFactory()

    print("\nTesting Creature with transform capability")

    base_t = transform_factory.create_base()
    print(" base:")
    print(base_t.describe())
    print(base_t.attack())
    print(base_t.transform())
    print(base_t.attack())
    print(base_t.revert())

    evolved_t = transform_factory.create_evolved()
    print(" evolved:")
    print(evolved_t.describe())
    print(evolved_t.attack())
    print(evolved_t.transform())
    print(evolved_t.attack())
    print(evolved_t.revert())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
