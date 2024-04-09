import tkinter as tk
import random as rand

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import graph

data = []

for i in range (5):
    data.append(dict([("2024-4-8", rand.randint(-5, 35)), ("2024-4-9", rand.randint(-5, 35)), ("2024-4-10", rand.randint(-5, 35)), ("2024-4-11", rand.randint(-5, 35)), ("2024-4-12", rand.randint(-5, 35)), ("2024-4-13", rand.randint(-5, 35))]))

def createWindow():
    window = tk.Tk()
    window.title('test')
    window.grid()
    return window

def createGraphWidget(window):
    figure = graph.createGraph(data)
    figure_canvas = FigureCanvasTkAgg(figure, window)
    figure_canvas.get_tk_widget().grid(column=1, row=0, rowspan=2)

def createStandardWidget(window):
    tk.Button(window, text="Générer le Graphique\nd'évolution des températures", command=createGraphWidget(window)).grid(column=0, row=0)
    tk.Button(window, text="Quit", command=window.destroy).grid(column=0, row=1)

mainWindow = createWindow()
createStandardWidget(mainWindow)

mainWindow.mainloop()