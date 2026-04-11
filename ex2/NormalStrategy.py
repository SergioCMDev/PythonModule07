from .BattleStrategy import BattleStrategy
from ex0 import Creature


class NormalStrategy (BattleStrategy):
    def act(self, criature: Creature):
        print(criature.attack())

    def is_valid(self, criature: Creature) -> bool:
        if (criature is None):
            return False
        if (isinstance(criature, Creature)):
            return True
        return False
