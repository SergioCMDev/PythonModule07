from .BattleStrategy import BattleStrategy
from ex0 import Creature


class NormalStrategy (BattleStrategy):
    def act(criature: Creature):
        criature.attack()

    def is_valid(self, criature: Creature) -> bool:
        if (criature is None):
            return False
        if (criature is Creature):
            return True
