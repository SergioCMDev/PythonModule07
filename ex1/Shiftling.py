from ex0 import Creature
from .TransformCapability import TransformCapability


class Shiftling (Creature, TransformCapability):

    def transform(self, target) -> str:
        return "Blomelle transform"

    def revert(self, target) -> str:
        return "Shiftling revert"
