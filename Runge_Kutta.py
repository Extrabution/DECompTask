from DifferentialEq import DifferentialEq
import math


class RungeKutta(DifferentialEq):
    def calculation(self, sols):
        k1i = (1/math.cos(sols[0])) - sols[1]*math.tan(sols[0])
        xi = sols[0] + self.h/2
        yk2i = sols[1] + self.h/2*k1i
        k2i = (1/math.cos(xi)) - yk2i*math.tan(xi)
        yk3i = sols[1] + self.h/2*k2i
        k3i = (1 / math.cos(xi)) - yk3i * math.tan(xi)
        yk4i = sols[1] + self.h*k3i
        k4i = (1 / math.cos(sols[0] + self.h)) - yk4i * math.tan(sols[0] + self.h)
        newy = sols[1] + self.h / 6 * (k1i + 2*k2i + 2*k3i + k4i)
        newx = sols[0] + self.h
        return [newx, newy]

    def solution(self, exact):
        self.solutions = [[self.x0, self.y0]]
        for i in range(self.n):
            if not (math.fabs(self.x0 + i * self.h - math.pi / 2) < 3 / 2 * self.h or \
                    math.fabs(self.x0 + i*self.h - 3*math.pi/2) < 3/2*self.h):
                self.solutions.append(self.calculation(self.solutions[i]))
                self.solutionsx.append(self.solutions[i][0])
                self.solutionsy.append(self.solutions[i][1])
            else:
                self.solutions.append(exact[i])
                print("catch ", self.solutions[-1][0])
                self.solutionsx.append(self.solutions[-1][0])
                self.solutionsy.append(self.solutions[-1][1])

    def errors_local_comp(self, exact, sols):
        t = exact - sols[1] - self.h * ((1 / math.cos(sols[0])) - sols[1] * math.tan(sols[0]))
        return t

    def local_errors_computation(self, exact):
        for i in range(self.n - 1):
            self.local_errors.append(self.errors_local_comp(exact.solutions[i + 1][1], self.solutions[i]))
            self.le_x.append(self.solutions[i][0])

    def errors_global_comp(self, exact, sols):
        t = math.fabs(sols[1] - exact)
        return t

    def global_errors_computation(self, exact):
        for i in range(self.n):
            self.global_errors.append(self.errors_global_comp(exact.solutions[i][1], self.solutions[i]))
            self.ge_x.append(self.solutions[i][0])