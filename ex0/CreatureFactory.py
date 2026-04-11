from abc import ABC, abstractmethod
from .Creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass
