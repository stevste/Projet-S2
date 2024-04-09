import tkinter as tk
import random as rand

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import graph

data = []

for i in range (5):
    data.append(dict([("2024-4-8", rand.randint(-5, 35)), ("2024-4-9", rand.randint(-5, 35)), ("2024-4-10", rand.randint(-5, 35)), ("2024-4-11", rand.randint(-5, 35)), ("2024-4-12", rand.randint(-5, 35)), ("2024-4-13", rand.randint(-5, 35))]))

window = tk.Tk()
window.title('test')
window.grid()

figure = graph.createGraph(data)
figure_canvas = FigureCanvasTkAgg(figure, window)

tk.Button(window, text="Quit", command=window.destroy).grid(column=0, row=1)
graphWidget = figure_canvas.get_tk_widget().grid(column=0, row=0)

window.mainloop()