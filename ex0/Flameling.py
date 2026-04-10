from ex0.Creature import Creature


class Flameling(Creature):
    def __init__(self, name):
        super().__init__(name, "Flameling")

    def attack(self) -> str:
        super().attack()
        return "Flame"
