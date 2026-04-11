from .CreatureFactory import CreatureFactory
from .Pyrodon import Pyrodon
from .Flameling import Flameling
from .Creature import Creature


class FlameFactory(CreatureFactory):
    def create_base(self, name: str = "Flameling") -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str = "Pyrodon") -> Creature:
        return Pyrodon(name)
