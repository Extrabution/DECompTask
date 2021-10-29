from abc import ABC, abstractmethod


class Computation(ABC):

    def __init__(self):
        return

    @abstractmethod
    def solve(self, x0, y):
        pass

    @abstractmethod
    def getComputedValues(self):
        pass

    @abstractmethod
    def getErrors(self):
        pass
