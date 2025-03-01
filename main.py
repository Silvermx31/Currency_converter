import tkinter as tk
from Model import Model
from View import View

if __name__ == "__main__":
    converter = Model()
    root = tk.Tk()
    app = View(root, converter)
    root.mainloop()