# from typing import TypeGuard

from ex1.TransformCapability import TransformCapability
from ex1.HealCapability import HealCapability

from .BattleStrategy import BattleStrategy
from ex0 import Creature


class AggressiveStrategy (BattleStrategy):
    def act(self, criature: Creature):
        if (not self.is_valid(criature)):
            raise Exception("Criatura is not valid")
        if (not isinstance(criature, TransformCapability)):
            return
        print(criature.transform())
        print(criature.attack())
        print(criature.revert())

    def is_valid(self, criature: Creature) -> bool:
        if (criature is None):
            return False
        if (not isinstance(criature, HealCapability)
                and not isinstance(criature, TransformCapability)):
            return False
        if (isinstance(criature, TransformCapability)):
            return True
        return False

    # def is_valid2(self, criature: Creature)
    # -> TypeGuard[TransformCapability]:
    #     if (criature is None):
    #         return False
    #     if (isinstance(criature, TransformCapability)):
    #         return True
    #     return False
