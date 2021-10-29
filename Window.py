import PySimpleGUI as psg
from EulerMethod import Euler
from ImprovedEulerMethod import ImprovedEuler
from Runge_Kutta import RungeKutta
from ExactSolutionMethod import ExactSolution
from Plotting import Plot

class Window:
    def __init__(self):
        self.event = None
        self.values = None
        self.graph_layout = [[psg.Text("Graph")], [psg.Canvas(size=(350, 300), key="Main_graph")]]
        self.graph3_layout = [[psg.Canvas(size=(200, 200), key="local")]]
        self.graph2_layout = [[psg.Canvas(size=(200, 200), key="global")]]
        self.graph_local_errors_layout = [
            [psg.Text("Local Errors")], [psg.Frame(title="", layout=self.graph2_layout)]
        ]
        self.graph_total_errors_layout = [
            [psg.Text("Total Errors")], [psg.Frame(title="", layout=self.graph3_layout)]
        ]
        self.button_frame_layout = [
            [psg.Text("Variables")],
            [psg.Text("x0"), psg.In("0", size=20, enable_events=True, key="x0")],
            [psg.Text("y0"), psg.In("1", size=20, enable_events=True, key="y0")],
            [psg.Text("N "), psg.In("30", size=20, enable_events=True, key="N")],
            [psg.Text("X "), psg.In("7", size=20, enable_events=True, key="X")],
            [psg.Text("n0 "), psg.In("1", size=20, enable_events=True, key="n0")],
            [psg.Checkbox(text="Euler's Method", enable_events=True, default=True, key="EM")],
            [psg.Checkbox(text="Improved Euler's Method", enable_events=True, default=True, key="IEM")],
            [psg.Checkbox(text="Runge-Kutta Method", enable_events=True, default=True, key="RK")],
            [psg.Checkbox(text="Exact Solution", enable_events=True, default=True, key="ES")],
            [psg.Button(button_text="Show", key="show")]
        ]

        self.buttons_layout = [[psg.Text("Variables:")], [psg.Frame("", layout=self.button_frame_layout)]]
        self.top_layout = [[psg.Column(self.graph_layout), psg.Column(self.buttons_layout)]]
        self.bottom_layout = [[psg.Column(self.graph_local_errors_layout), psg.Column(self.graph_total_errors_layout)]]
        self.window_layout = [self.top_layout, self.bottom_layout]
        self.window = psg.Window(title="Inchin Ivan", layout=self.window_layout,
                            size=(750, 600), margins=(20, 5))

    def generate_window(self):
        euler = Euler(0, 1, 7, 30,1)
        improvedeuler = ImprovedEuler(0, 1, 7, 30,1)
        runge = RungeKutta(0, 1, 7, 30,1)
        exact = ExactSolution(0, 1, 7, 30,1)
        plotting = Plot()
        events = ["x0", "y0", "N", "X", "EM", "IEM", "RK", "ES", "n0"]
        while True:
            self.event, self.values = self.window.read()
            if self.event == psg.WIN_CLOSED:
                break
            elif self.event in events:
                euler.x0 = int(self.values["x0"])
                euler.y0 = int(self.values["y0"])
                euler.n = int(self.values["N"])
                euler.x = int(self.values["X"])
                euler.n0 = int(self.values["n0"])
                improvedeuler.x0 = int(self.values["x0"])
                improvedeuler.y0 = int(self.values["y0"])
                improvedeuler.n = int(self.values["N"])
                improvedeuler.x = int(self.values["X"])
                improvedeuler.n0 = int(self.values["n0"])
                runge.x0 = int(self.values["x0"])
                runge.y0 = int(self.values["y0"])
                runge.n = int(self.values["N"])
                runge.x = int(self.values["X"])
                runge.n0 = int(self.values["n0"])
                exact.x0 = int(self.values["x0"])
                exact.y0 = int(self.values["y0"])
                exact.n = int(self.values["N"])
                exact.x = int(self.values["X"])
                exact.n0 = int(self.values["n0"])
                euler.h = (euler.x - euler.x0) / euler.n
                improvedeuler.h = (improvedeuler.x - improvedeuler.x0) / improvedeuler.n
                runge.h = (runge.x - runge.x0) / runge.n
                exact.h = (exact.x - exact.x0) / exact.n
            elif self.event == "show":
                exact.solutions = list()
                exact.solutionsy.clear()
                exact.solutionsx.clear()
                exact.solution(None)
                if self.values["EM"]:
                    euler.solutions = list()
                    euler.solutionsy.clear()
                    euler.solutionsx.clear()
                    euler.solution(exact.solutions)
                    euler.local_errors = list()
                    euler.le_x = list()
                    euler.local_errors_computation(exact)
                    euler.global_errors = list()
                    euler.ge_x = list()
                    euler.global_errors_computation(exact)

                if self.values["IEM"]:
                    improvedeuler.solutions = list
                    improvedeuler.solutionsy.clear()
                    improvedeuler.solutionsx.clear()
                    improvedeuler.solution(exact.solutions)
                    improvedeuler.local_errors = list()
                    improvedeuler.le_x = list()
                    improvedeuler.local_errors_computation(exact)
                    improvedeuler.global_errors = list()
                    improvedeuler.ge_x = list()
                    improvedeuler.global_errors_computation(exact)

                if self.values["RK"]:
                    runge.solutions = list
                    runge.solutionsy.clear()
                    runge.solutionsx.clear()
                    runge.solution(exact.solutions)
                    runge.local_errors = list()
                    runge.le_x = list()
                    runge.local_errors_computation(exact)
                    runge.global_errors = list()
                    runge.ge_x = list()
                    runge.global_errors_computation(exact)
                if self.values["ES"]:
                    exact.solutions = list
                    exact.solutionsy.clear()
                    exact.solutionsx.clear()
                    exact.solution(None)

                plotting.plot_graph(self.window['Main_graph'].TKCanvas, self.window['local'].TKCanvas,
                                                     self.window['global'].TKCanvas,
                                                     euler, improvedeuler, runge, exact,
                                                     self.values["EM"], self.values["IEM"],
                                                     self.values["RK"], self.values["ES"])

        self.window.close()