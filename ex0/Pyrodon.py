from .Creature import Creature


class Pyrodon(Creature):
    def __init__(self, name):
        super().__init__(name, "Pyrodon")

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower."
