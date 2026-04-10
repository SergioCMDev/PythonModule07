
from .Creature import Creature


class Torragon(Creature):
    def __init__(self, name):
        super().__init__(name, "Torragon")

    def attack(self) -> str:
        super().attack()
        return f"{self._name} uses hydro Pump"
