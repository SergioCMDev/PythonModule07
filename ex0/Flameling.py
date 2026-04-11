from .Creature import Creature


class Flameling(Creature):
    def __init__(self, name: str = "Flameling"):
        super().__init__(name, "Flameling")

    def attack(self) -> str:
        super().attack()
        return f"{self._name} uses Ember."
