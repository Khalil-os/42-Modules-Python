from collections.abc import Callable
from typing import List


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (
        spell1(target, power),
        spell2(target, power),
    )


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )


def spell_sequence(spells: List[Callable]) -> Callable:
    return lambda target, power: [
        spell(target, power) for spell in spells
    ]


def main():
    target = "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined(target, 10)
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    print("Original: 10, Amplified: 30")


if __name__ == "__main__":
    main()
