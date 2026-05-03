from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) >= 3:
                power = args[2]
            else:
                power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt "
                              f"{attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def failing_spell():
    raise Exception("fail")


@retry_spell(3)
def success_spell():
    return "Waaaaaaagh spelled !"


def main():
    print("Testing spell timer...")
    result = fireball()
    print("Result:", result)

    print("\nTesting retrying spell...")
    print(failing_spell())
    print(success_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("A1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
