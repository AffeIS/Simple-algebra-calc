import re
import sympy
import tkinter as tk
from tkinter import ttk

def calculate(x, y, operation, simplify):
    def process_input(input_str):
        input_str = re.sub(r'(\d+)([a-z])', r'\1*\2', input_str)
        input_str = re.sub(r'([a-z])\*\*(\d+)', r'\1^\2', input_str)
        try:
            return sympy.sympify(input_str)
        except sympy.SympifyError:
            print("Invalid input. Please enter a valid numeric value or algebraic expression.")
            return None

    x = process_input(x)
    y = process_input(y)

    if x is None or y is None:
        return None

    expr = f"({x}) {operation} ({y})"
    simplified_expr = sympy.simplify(expr) if simplify else expr
    return str(simplified_expr).replace('**', '^')

def on_calculate():
    operation = operation_var.get()
    x = entry_x.get()
    y = entry_y.get()
    simplify = simplify_var.get() == 1

    result = calculate(x, y, operation, simplify)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Algebraic Calculator")

# Create and set up widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

operation_var = tk.StringVar()
operation_label = ttk.Label(frame, text="Select operation:")
operation_combobox = ttk.Combobox(frame, textvariable=operation_var, values=["+", "-", "*", "/"])
operation_combobox.set("+")

entry_x = ttk.Entry(frame, width=15)
entry_y = ttk.Entry(frame, width=15)

simplify_var = tk.IntVar()
simplify_checkbox = ttk.Checkbutton(frame, text="Simplify", variable=simplify_var)

calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)

result_label = ttk.Label(frame, text="Result: ")

# Arrange widgets in the grid
operation_label.grid(column=0, row=0, sticky=tk.W)
operation_combobox.grid(column=1, row=0, sticky=tk.W)
entry_x.grid(column=0, row=1, sticky=tk.W)
entry_y.grid(column=1, row=1, sticky=tk.W)
simplify_checkbox.grid(column=0, row=2, sticky=tk.W)
calculate_button.grid(column=1, row=2, sticky=(tk.W, tk.E))
result_label.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.E))

# Run the application
root.mainloop()
