import tkinter as tk
from tkinter import ttk, messagebox
from Model import Model


class View:
    def __init__(self, root, converter):
        self.converter = converter
        self.root = root
        self.root.title("Valuuta kalkulaator")
        self.root.geometry("300x200")
        self.center_window()

        self.from_label = ttk.Label(root, text="Millest:")
        self.from_label.pack()
        self.from_currency = ttk.Combobox(root, values=self.converter.supported_currencies, state='readonly')
        self.from_currency.pack()

        self.to_label = ttk.Label(root, text="Milleks:")
        self.to_label.pack()
        self.to_currency = ttk.Combobox(root, values=self.converter.supported_currencies, state='readonly')
        self.to_currency.pack()

        self.amount_label = ttk.Label(root, text="Kogus:")
        self.amount_label.pack()
        self.amount_entry = ttk.Entry(root, validate='key')
        self.amount_entry.configure(validatecommand=(self.root.register(self.validate_amount), '%P'))
        self.amount_entry.pack()


        self.convert_button = ttk.Button(root, text="Konverteeri", command=self.convert)
        self.convert_button.pack()

        self.result_label = ttk.Label(root, text="Tulemus:")
        self.result_label.pack()
        self.amount_entry.bind('<Return>', lambda event: self.convert())

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def convert(self):
        try:
            amount = float(self.sanitize_amount(self.amount_entry.get()))
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            result = self.converter.convert(amount, from_currency, to_currency)
            self.result_label.config(text=f"Tulemus: {result} {to_currency}")
        except ValueError:
            messagebox.showerror("Viga", "Kogus sisestamata")
        except Exception as e:
            messagebox.showerror("Viga", str(e))

    def sanitize_amount(self, amount):
        return amount.replace(',', '.')

    def validate_amount(self, value):
        if value == "" or (value.replace(',', '.').count('.') <= 1 and value.replace(',', '').replace('.', '').isdigit()):
            return True
        messagebox.showerror("Viga.", "Vale kogus!")
        return False