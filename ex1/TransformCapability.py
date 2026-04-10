from abc import ABC, abstractmethod


class TransformCapability(ABC):

    @abstractmethod
    def transform(self, target):
        pass

    @abstractmethod
    def revert(self, target):
        pass
