from alchemy.grimoire import record_spell, validate_ingredients
from alchemy.grimoire.spellbook import record_spell_injected

print("=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print('validate_ingredients("fire air"):',
      validate_ingredients("fire air"))
print('validate_ingredients("dragon scales"):',
      validate_ingredients("dragon scales"))

print("\nTesting spell recording with validation:")
print('record_spell("Fireball", "fire air"):',
      record_spell("Fireball", "fire air"))
print('record_spell("Dark Magic", "shadow"):',
      record_spell("Dark Magic", "shadow"))

print("\nTesting late import technique:")
print('record_spell("Lightning", "air"):',
      record_spell("Lightning", "air"))

print("\nTesting dependency injection technique:")
print('record_spell_injected("Lightning", "air"):',
      record_spell_injected("Lightning", "air", validate_ingredients))

print("\nCircular dependency curse avoided using multiple techniques!")
print("All spells processed safely!")
