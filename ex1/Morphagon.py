from ex0 import Creature
from .TransformCapability import TransformCapability


class Morphagon (Creature, TransformCapability):
    def transform(self, target) -> str:
        return "Morphagon transform"

    def revert(self, target) -> str:
        return "Morphagon revert"
