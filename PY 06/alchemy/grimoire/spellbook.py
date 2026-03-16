from typing import Callable


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"


def record_spell_injected(spell_name: str, ingredients: str,
                          validator: Callable[[str], str]) -> str:

    result = validator(ingredients)

    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
