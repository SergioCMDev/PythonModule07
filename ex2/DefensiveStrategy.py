from ex1.HealCapability import HealCapability
from ex1.TransformCapability import TransformCapability

from ex0 import Creature

from .BattleStrategy import BattleStrategy


class DefensiveStrategy (BattleStrategy):
    def act(self, criature: Creature):
        if (not self.is_valid(criature)):
            raise "Criatura is not valid"
        if (not isinstance(criature, TransformCapability)):
            return
        criature.attack()
        criature.heal()

    def is_valid(criature: Creature) -> bool:
        if (criature is None):
            return False
        if (not isinstance(criature, HealCapability)
                or not isinstance(criature, TransformCapability)):
            return False
        if (isinstance(criature, HealCapability)):
            return True
        return False
