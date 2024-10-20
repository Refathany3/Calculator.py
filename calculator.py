
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display numbers
display = tk.Entry(root, width=25, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click event
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_add():
    first_number = display.get()
    global f_num
    global operation
    operation = "add"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if operation == "add":
        display.insert(0, f_num + int(second_number))

# Define buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_add = tk.Button(root, text="+", padx=20, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)

# Positioning buttons
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_equal.grid(row=2, column=3)
button_clear.grid(row=2, column=2)

# Running the app
root.mainloop()
