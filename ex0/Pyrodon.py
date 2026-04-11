from .Creature import Creature


class Pyrodon(Creature):
    def __init__(self, name):
        super().__init__(name, "Pyrodon")

    def attack(self) -> str:
        super().attack()
        return f"{self._name} uses Flamethrower."
