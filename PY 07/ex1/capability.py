from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        """Heal action."""


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Transform state."""

    @abstractmethod
    def revert(self) -> str:
        """Return to normal state."""
