from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class StrategyError(Exception):
    """Invalid strategy-creature combination."""


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check if strategy fits creature."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Apply strategy."""


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )

        transformer = creature
        print(transformer.transform())
        print(transformer.attack())
        print(transformer.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )

        healer = creature
        print(healer.attack())
        print(healer.heal())
