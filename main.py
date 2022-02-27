import tkinter as tk
from tkinter import messagebox
import numpy as np
import time

# ======================================================== GUI SET UP ====================================================
window = tk.Tk()

window.title("City Traffic Manager")
window.geometry("500x500")
window.configure(bg = "#474E64")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


# ======================================================== WIDGETS =======================================================

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Home")
btn_save = tk.Button(fr_buttons, text="Data Base")
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()

