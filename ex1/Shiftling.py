from ex0 import Creature
from .TransformCapability import TransformCapability


class Shiftling (Creature, TransformCapability):

    def __init__(self, name):
        super().__init__(name, "Shiftling")
        self.current_capability = ""

    def transform(self) -> str:
        self.current_capability = "Improved"
        return f"{self._name} shifts into a sharper form."

    def revert(self) -> str:
        self.current_capability = ""
        return f"{self._name} returns to normal"

    def attack(self) -> str:
        if (self.current_capability == "Improved"):
            return f"{self._name} mega-attack"
        return f"{self._name} attacks"
