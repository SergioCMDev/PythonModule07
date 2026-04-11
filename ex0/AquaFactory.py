from .CreatureFactory import CreatureFactory
from .Aquabub import Aquabub
from .Torragon import Torragon
from .Creature import Creature


class AquaFactory(CreatureFactory):
    def create_base(self, name: str = "Aquabub") -> Creature:
        return Aquabub(name)

    def create_evolved(self, name: str = "Torragon") -> Creature:
        return Torragon(name)
