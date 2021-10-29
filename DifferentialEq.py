from abc import ABCMeta, abstractmethod


class DifferentialEq(metaclass=ABCMeta):
    def __init__(self, _x0, _y0, _x, _n: int, _n0):
        self.x0 = _x0
        self.x = _x
        self.y0 = _y0
        self.n = _n
        self.n0 = _n0
        self.h = (self.x - self.x0) / self.n
        self.solutions = list
        self.solutionsx = []
        self.solutionsy = []
        self.local_errors = []
        self.le_x = []
        self.global_errors = []
        self.ge_x = []

    @abstractmethod
    def calculation(self, sols):
        pass

    @abstractmethod
    def solution(self, exact):
        pass

    @abstractmethod
    def errors_local_comp(self, exact, sols):
        pass

    @abstractmethod
    def local_errors_computation(self, exact):
        pass

    @abstractmethod
    def errors_global_comp(self, exact, sols):
        pass

    @abstractmethod
    def global_errors_computation(self, exact):
        pass