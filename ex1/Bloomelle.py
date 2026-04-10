from ex0 import Creature
from . import HealCapability


class Bloomelle(Creature, HealCapability):

    def heal(self, target) -> str:
        return "Blomelle heal"
