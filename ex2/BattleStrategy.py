from abc import ABC, abstractmethod
from ex0 import Creature


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, criature: Creature):
        pass

    @abstractmethod
    def is_valid(self, criature: Creature) -> bool:
        pass
