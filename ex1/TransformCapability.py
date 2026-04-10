from abc import ABC, abstractmethod


class TransformCapability(ABC):
    current_capability = ""

    @abstractmethod
    def transform(target):
        pass

    @abstractmethod
    def revert(target):
        pass
