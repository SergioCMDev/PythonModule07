
from .Creature import Creature


class Torragon(Creature):
    def __init__(self, name):
        super().__init__(name, "Torragon")

    def attack(self) -> str:
        return f"{self._name} uses hydro Pump."
