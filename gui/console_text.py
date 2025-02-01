import tkinter as tk

class ConsoleText(tk.Text):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    # 읽기 전용
    self.config(state=tk.DISABLED)

  def write(self, message):
    self.config(state=tk.NORMAL)
    self.insert(tk.END, message)
    self.see(tk.END)
    self.config(state=tk.DISABLED)

  def flush(self):
    pass