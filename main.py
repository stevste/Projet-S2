import tkinter as tk
import random as rand

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import graph

window = tk.Tk()
window.title('test')
window.grid()

figure = graph.createGraph()
figure_canvas = FigureCanvasTkAgg(figure, window)

tk.Button(window, text="Quit", command=window.destroy).grid(column=0, row=1)
graphWidget = figure_canvas.get_tk_widget().grid(column=0, row=0)

window.mainloop()