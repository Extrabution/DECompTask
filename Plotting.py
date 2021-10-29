import PySimpleGUI as psg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot


def draw_graph(fig, canvas):
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    figure_canvas_agg.get_tk_widget()
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=0)
    return figure_canvas_agg


class Plot:
    def __init__(self):
        self.flag = 0
        self.figure_canvas_agg_saved: FigureCanvasTkAgg
        self.figure_canvas_agg_saved_local: FigureCanvasTkAgg
        self.figure_canvas_agg_saved_global: FigureCanvasTkAgg

    def plot_graph(self, canvas, canvas_local, canvas_global, euler, imrovedeuler, runge, exact, em, iem, rk, es):
        matplotlib.use('TkAgg')
        #fig = plt.figure(figsize=(5, 5), dpi=65)
        fig, ax = plt.subplots(1, sharex="all", sharey="all")
        fig_local, ax_local = plt.subplots(1, sharex="all", sharey="all")
        fig_global, ax_global = plt.subplots(1, sharex="all", sharey="all")
        if em:
            ax.plot(euler.solutionsx, euler.solutionsy, label="Euler", color="Red")
            ax_local.plot(euler.le_x, euler.local_errors, label="Euler", color="Red")
            ax_global.plot(euler.ge_x, euler.global_errors, label="Euler", color="Red")
        if iem:
            ax.plot(imrovedeuler.solutionsx, imrovedeuler.solutionsy, label="Improved Euler", color="Blue")
            ax_local.plot(imrovedeuler.le_x, imrovedeuler.local_errors, label="Improved Euler", color="Blue")
            ax_global.plot(imrovedeuler.ge_x, imrovedeuler.global_errors, label="Improved Euler", color="Blue")
        if rk:
            ax.plot(runge.solutionsx, runge.solutionsy, label="Runge-Kutta", color="Yellow")
            ax_local.plot(runge.le_x, runge.local_errors, label="Runge-Kutta", color="Yellow")
            ax_global.plot(runge.ge_x, runge.global_errors, label="Runge-Kutta", color="Yellow")
        if es:
            ax.plot(exact.solutionsx, exact.solutionsy, label="Exact", color="magenta")
        ax.grid("on")
        ax_local.grid("on")
        ax_global.grid("on")
        if em or iem or rk:
            ax.legend(loc="best", fontsize='xx-small')
            ax_local.legend(loc="best", fontsize='xx-small')
            ax_global.legend(loc="best", fontsize='xx-small')
        if self.flag == 1:
            self.figure_canvas_agg_saved.get_tk_widget().forget()
            self.figure_canvas_agg_saved_local.get_tk_widget().forget()
            self.figure_canvas_agg_saved_global.get_tk_widget().forget()

        fig.set_size_inches(5, 3.2)
        fig_local.set_size_inches(3, 2)
        fig_global.set_size_inches(3, 2)
        self.figure_canvas_agg_saved = draw_graph(fig, canvas)
        self.figure_canvas_agg_saved_local = draw_graph(fig_local, canvas_local)
        self.figure_canvas_agg_saved_global = draw_graph(fig_global, canvas_global)
        self.flag = 1

