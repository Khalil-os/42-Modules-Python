from typing import List, Tuple

from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError,
)


Opponent = Tuple[CreatureFactory, BattleStrategy]


def tournament(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_one, strategy_one = opponents[i]
                factory_two, strategy_two = opponents[j]

                creature_one = factory_one.create_base()
                creature_two = factory_two.create_base()

                print("\n* Battle *")
                print(creature_one.describe())
                print(" vs.")
                print(creature_two.describe())
                print(" now fight!")

                strategy_one.act(creature_one)
                strategy_two.act(creature_two)

    except StrategyError as error:
        print(
            "Battle error, aborting tournament:",
            error
        )


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")

    tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")

    tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )

    tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
