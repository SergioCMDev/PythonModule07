from abc import ABC, abstractmethod


class Creature (ABC):
    def __init__(self, name: str, type: str):
        super().__init__()
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} type {self._type}"
