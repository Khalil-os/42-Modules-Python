from __future__ import annotations

from abc import ABC, abstractmethod

from .creature import (
    Creature,
    Flameling,
    Pyrodon,
    Aquabub,
    Torragon,
)


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Create base creature."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create evolved creature."""


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
