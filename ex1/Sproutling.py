from typing import Optional
from ex0 import Creature
from .HealCapability import HealCapability


class Sproutling(Creature, HealCapability):

    def __init__(self, name):
        super().__init__(name, "Sproutling")

    def heal(self, target: Optional[Creature] = None) -> str:
        if target is not None:
            return f"{self._name} heals {target._name}"
        return f"{self._name} heals itself"

    def attack(self) -> str:
        return f"{self._name} attack"
