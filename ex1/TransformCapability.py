from abc import ABC, abstractmethod


class TransformCapability(ABC):

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass
