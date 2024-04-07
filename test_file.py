import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# using ttk gives the entry field and button a more modern look


root = tk.Tk()

root.title("Inches to Meters Converter")

canvas = tk.Canvas(root, width=500, height=130)
canvas.grid(columnspan=3, rowspan=2)


# Input Section
input_prompt = tk.Label(root, text="Inches:")
input_prompt.grid(column=0, row=0)

# Input Field
inches_tk = tk.IntVar()
input_field = ttk.Entry(root, textvariable= inches_tk)
input_field.grid(row= 0, column=1)


# Convert Button Function
def convert():
    try:  # tries this code and goes to except if there is an error
        inches = inches_tk.get()
        meters = round(inches / 39.37, 4)

        # Result Value Label
        result_value = tk.Label(root, text=meters)
        result_value.grid(row=1, column=1)
    except tk._tkinter.TclError:  # this code is run if there is an error
        messagebox.showwarning("Input Warning", "Invalid Input")


# Convert Button
convert_btn = ttk.Button(root, text="Convert", command=lambda:convert())
convert_btn.grid(row=0, column=2)

# Result Label
result_label = tk.Label(root, text="Meters:")
result_label.grid(row=1, column=0)


root.mainloop()
