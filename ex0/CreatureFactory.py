from abc import ABC, abstractmethod
from .Creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(name: str) -> Creature:
        pass
