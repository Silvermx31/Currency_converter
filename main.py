import tkinter as tk
from Model import Model
from View import CurrencyConverterGUI

if __name__ == "__main__":
    converter = Model()
    root = tk.Tk()
    app = CurrencyConverterGUI(root, converter)
    root.mainloop()