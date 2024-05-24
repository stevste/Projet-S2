import tkinter as tk

class UpdateLabel(tk.Label):
  def __init__(self, *args, **kwargs):
    tk.Label.__init__(self, *args, **kwargs)
    self._count = 0

  def update_text(self):
    self.config(text=str(self._count))
    self._count += 1
    self.after(2000, self.update_text)

root = tk.Tk()
label = UpdateLabel(root)
label.pack()
label.update_text()
root.mainloop()