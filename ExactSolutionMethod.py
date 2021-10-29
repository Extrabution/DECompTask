from DifferentialEq import DifferentialEq
import math
import numpy as np


class ExactSolution(DifferentialEq):
    def calculation(self, sols):
        newx = sols[0] + self.h
        newy = math.sin(newx) + math.cos(newx)

        return [newx, newy]

    def solution(self, exact):
        self.solutions = [[self.x0, self.y0]]
        for i in range(self.n):
            self.solutionsx.append(self.solutions[i][0])
            self.solutionsy.append(self.solutions[i][1])
            self.solutions.append(self.calculation(self.solutions[i]))

    def errors_local_comp(self, exact, sols):
        pass

    def local_errors_computation(self, exact):
        pass

    def errors_global_comp(self, exact, sols):
        pass

    def global_errors_computation(self, exact):
        pass
