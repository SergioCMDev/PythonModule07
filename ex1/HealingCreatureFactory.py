from ex0 import CreatureFactory
from .Bloomelle import Bloomelle
from .Sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):

    def create_base(self, name: str = "Sproutling") -> Sproutling:
        return Sproutling(name)

    def create_evolved(self, name: str = "Bloomelle") -> Bloomelle:
        return Bloomelle(name)
