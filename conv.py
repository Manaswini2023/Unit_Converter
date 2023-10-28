import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def convert():
    value_str = entry_value.get()
    try:
        value = float(value_str)
        source_unit = source_unit_var.get()
        target_unit = target_unit_var.get()

        if source_unit == "Celsius" and target_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(value)
            result_label.config(text=f"{value} °C is equal to {result:.2f} °F.", foreground="green")
        elif source_unit == "Fahrenheit" and target_unit == "Celsius":
            result = fahrenheit_to_celsius(value)
            result_label.config(text=f"{value} °F is equal to {result:.2f} °C.", foreground="green")
        elif source_unit == "Meters" and target_unit == "Feet":
            result = meters_to_feet(value)
            result_label.config(text=f"{value} meters is equal to {result:.2f} feet.", foreground="green")
        elif source_unit == "Feet" and target_unit == "Meters":
            result = feet_to_meters(value)
            result_label.config(text=f"{value} feet is equal to {result:.2f} meters.", foreground="green")
        elif source_unit == "Kilograms" and target_unit == "Pounds":
            result = kilograms_to_pounds(value)
            result_label.config(text=f"{value} kilograms is equal to {result:.2f} pounds.", foreground="green")
        elif source_unit == "Pounds" and target_unit == "Kilograms":
            result = pounds_to_kilograms(value)
            result_label.config(text=f"{value} pounds is equal to {result:.2f} kilograms.", foreground="green")
        else:
            result_label.config(text="Unsupported units. Please select valid units.", foreground="red")
    except ValueError:
        result_label.config(text=f"Invalid input: '{value_str}' is not a valid numeric value.", foreground="red")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Maximize the window
window.state('zoomed')

# Set the background color of the root window
window.configure(bg="lightblue")

# Create and place widgets
frame = ttk.Frame(window, padding=10, style="TFrame")
frame.grid(column=0, row=0, sticky="nsew")

# Set the background color of the frame
style = ttk.Style()
style.configure("TFrame", background="lightblue")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

label_value = ttk.Label(frame, text="Enter the value:")
label_value.grid(column=0, row=0, columnspan=2, pady=5)

entry_value = ttk.Entry(frame, width=15)
entry_value.grid(column=0, row=1, columnspan=2, pady=5)

source_unit_var = tk.StringVar()
source_unit_var.set("Celsius")
target_unit_var = tk.StringVar()
target_unit_var.set("Fahrenheit")

label_source_unit = ttk.Label(frame, text="Select source unit:")
label_source_unit.grid(column=0, row=2, columnspan=2, pady=5)

source_unit_menu = ttk.Combobox(frame, textvariable=source_unit_var, values=["Celsius", "Fahrenheit", "Meters", "Feet", "Kilograms", "Pounds"], width=15)
source_unit_menu.grid(column=0, row=3, columnspan=2, pady=5)

label_target_unit = ttk.Label(frame, text="Select target unit:")
label_target_unit.grid(column=0, row=4, columnspan=2, pady=5)

target_unit_menu = ttk.Combobox(frame, textvariable=target_unit_var, values=["Celsius", "Fahrenheit", "Meters", "Feet", "Kilograms", "Pounds"], width=15)
target_unit_menu.grid(column=0, row=5, columnspan=2, pady=5)

convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(column=0, row=6, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=7, columnspan=2, pady=5)

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Start the main loop
window.mainloop()

