from ex0 import CreatureFactory, Creature
from .Bloomelle import Bloomelle
from .Sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):

    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)
