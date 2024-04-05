import numpy as np
from tkinter import *
import tkinter as tk
import matplotlib as plt

window = tk.Tk()
window.title('test')
window.geometry('1024x768')
window.config(bg='#F26849')
window.grid()

tk.Button(window, text="Quit", command=window.destroy).grid(column=0, row=1)
window.mainloop()