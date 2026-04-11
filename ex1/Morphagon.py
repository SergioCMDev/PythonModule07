from ex0 import Creature
from .TransformCapability import TransformCapability


class Morphagon (Creature, TransformCapability):

    def __init__(self,  name: str = "Morphagon"):
        super().__init__(name, "Morphagon")
        self.current_capability = ""

    def transform(self) -> str:
        self.current_capability = "Improved"
        return f"{self._name} morphs into a dragonic battle form."

    def revert(self) -> str:
        self.current_capability = ""
        return f"{self._name} revert transformation and stabilizes its form."

    def attack(self) -> str:
        if (self.current_capability == "Improved"):
            return f"{self._name} triattacks."
        return f"{self._name} attacks."
