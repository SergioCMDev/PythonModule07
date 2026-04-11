from ex0 import CreatureFactory
from .Shiftling import Shiftling
from .Morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):

    def create_base(self, name: str = "Shiftling") -> Shiftling:
        return Shiftling(name)

    def create_evolved(self, name: str = "Morphagon") -> Morphagon:
        return Morphagon(name)
