from .CreatureFactory import CreatureFactory
from .Pyrodon import Pyrodon
from .Flameling import Flameling
from .Creature import Creature


class FlameFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        return Pyrodon(name)
