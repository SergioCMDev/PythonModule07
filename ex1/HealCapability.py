from abc import ABC, abstractmethod
from typing import Optional
from ex0 import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Optional[Creature] = None) -> str:
        pass
