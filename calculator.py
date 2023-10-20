import tkinter as tk

# Function to update the display
def update_display(value):
    current = display_var.get()
    if current == "0" or current == "Invalid input":
        display_var.set(value)
    else:
        display_var.set(current + value)

# Function to calculate and update the result
def calculate():
    try:
        expression = display_var.get()
        result = str(eval(expression))
        display_var.set(result)
    except:
        display_var.set("Invalid input")

# Function to clear the display
def clear():
    display_var.set("0")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display the input and result
display_var = tk.StringVar()
display_var.set("0")
display = tk.Entry(window, textvariable=display_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define the button layout
button_layout = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '%', '.', '=', '+'
]

# Create and place the buttons
row, col = 1, 0
for button_text in button_layout:
    if button_text == '=':
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Helvetica", 15), command=calculate).grid(row=row, column=col)
    elif button_text in ('0', '%'):
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Helvetica", 15), command=lambda x=button_text: update_display(x)).grid(row=row, column=col)
    else:
        tk.Button(window, text=button_text, padx=20, pady=20, font=("Helvetica", 15), command=lambda x=button_text: update_display(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = tk.Button(window, text="C", padx=20, pady=20, font=("Helvetica", 15), command=clear)
clear_button.grid(row=row, column=col)

# Start the main event loop
window.mainloop()
