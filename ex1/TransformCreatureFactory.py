from ex0 import CreatureFactory, Creature
from .Shiftling import Shiftling
from .Morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):

    def create_base(self, name: str = "Shiftling") -> Creature:
        return Shiftling(name)

    def create_evolved(self, name: str = "Morphagon") -> Creature:
        return Morphagon(name)
