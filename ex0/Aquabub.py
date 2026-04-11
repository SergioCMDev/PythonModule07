from .Creature import Creature


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub"):
        super().__init__(name, "Aquabub")

    def attack(self) -> str:
        super().attack()
        return f"{self._name} uses Water Gun."
