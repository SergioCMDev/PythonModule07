from ex0 import Creature
from .HealCapability import HealCapability


class Sproutling(Creature, HealCapability):

    def heal(self, target) -> str:
        return "Sproutling heal"
