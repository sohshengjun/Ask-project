import math
import tkinter as tk
from tkinter import messagebox

# Constants
pi = 3.142

# Volume and Surface Area functions
def calculate_cylinder_volume():
    r = float(entry_radius.get())
    h = float(entry_height.get())
    result = pi * r**2 * h
    messagebox.showinfo("Volume of Cylinder", f"The volume of the cylinder is {result:.2f}")

def calculate_cylinder_surface_area():
    r = float(entry_radius.get())
    h = float(entry_height.get())
    result = 2 * pi * r * (r + h)
    messagebox.showinfo("Surface Area of Cylinder", f"The surface area of the cylinder is {result:.2f}")

def calculate_cone_volume():
    r = float(entry_radius.get())
    h = float(entry_height.get())
    result = pi * r ** 2 * h / 3
    messagebox.showinfo("Volume of Cone", f"The volume of the cone is {result:.2f}")

def calculate_cone_surface_area():
    r = float(entry_radius.get())
    h = float(entry_height.get())
    result = pi * r * (r + math.sqrt(r**2 + h**2))
    messagebox.showinfo("Surface Area of Cone", f"The surface area of the cone is {result:.2f}")

def calculate_sphere_volume():
    r = float(entry_radius.get())
    result = (4.0/3.0) * pi * r**3
    messagebox.showinfo("Volume of Sphere", f"The volume of the sphere is {result:.2f}")

def calculate_sphere_surface_area():
    r = float(entry_radius.get())
    result = 4 * pi * r**2
    messagebox.showinfo("Surface Area of Sphere", f"The surface area of the sphere is {result:.2f}")

def calculate_cuboid_volume():
    l = float(entry_length.get())
    w = float(entry_width.get())
    h = float(entry_height.get())
    result = l * w * h
    messagebox.showinfo("Volume of Cuboid", f"The volume of the cuboid is {result:.2f}")

def calculate_cuboid_surface_area():
    l = float(entry_length.get())
    w = float(entry_width.get())
    h = float(entry_height.get())
    result = 2 * (l*w + l*h + w*h)
    messagebox.showinfo("Surface Area of Cuboid", f"The surface area of the cuboid is {result:.2f}")

# Modify the update_input_fields function
def update_input_fields(*args):
    selected_type = selected_prism.get()

    # Hide all input fields and labels
    label_radius.grid_forget()
    entry_radius.grid_forget()
    label_height.grid_forget()
    entry_height.grid_forget()
    label_length.grid_forget()
    entry_length.grid_forget()
    label_width.grid_forget()
    entry_width.grid_forget()

    # Show relevant input fields based on the selected prism type
    if selected_type == "Cylinder":
        label_radius.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        entry_radius.grid(row=0, column=1, padx=5, pady=2)
        label_height.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
        entry_height.grid(row=1, column=1, padx=5, pady=2)
    elif selected_type == "Cone":
        label_radius.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        entry_radius.grid(row=0, column=1, padx=5, pady=2)
        label_height.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
        entry_height.grid(row=1, column=1, padx=5, pady=2)
    elif selected_type == "Sphere":
        label_radius.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        entry_radius.grid(row=0, column=1, padx=5, pady=2)
    elif selected_type == "Cuboid":
        label_length.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        entry_length.grid(row=0, column=1, padx=5, pady=2)
        label_width.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
        entry_width.grid(row=1, column=1, padx=5, pady=2)
        label_height.grid(row=2, column=0, padx=5, pady=2, sticky=tk.E)
        entry_height.grid(row=2, column=1, padx=5, pady=2)

    # Update the command of the buttons based on the selected prism type
    calculate_volume_button.configure(command=calculate_volume_functions[selected_type])
    calculate_surface_area_button.configure(command=calculate_surface_area_functions[selected_type])

# Dictionary to map geometry type to volume calculation function
calculate_volume_functions = {
    "Cylinder": calculate_cylinder_volume,
    "Cone": calculate_cone_volume,
    "Sphere": calculate_sphere_volume,
    "Cuboid": calculate_cuboid_volume
}

# Dictionary to map geometry type to surface area calculation function
calculate_surface_area_functions = {
    "Cylinder": calculate_cylinder_surface_area,
    "Cone": calculate_cone_surface_area,
    "Sphere": calculate_sphere_surface_area,
    "Cuboid": calculate_cuboid_surface_area
}

root = tk.Tk()
root.title("Prism Calculator")
root.geometry("400x300")

# Labels
label_name_prism = tk.Label(root, text="Prism Type:")
label_name_prism.pack()

# Dropdown menu for selecting prism type
prism_types = ["Cylinder", "Cone", "Sphere", "Cuboid"]
selected_prism = tk.StringVar()
selected_prism.set(prism_types[0])  # Default to Cylinder
selected_prism.trace("w", update_input_fields)  # Call update_input_fields when dropdown value changes

prism_menu = tk.OptionMenu(root, selected_prism, *prism_types)
prism_menu.pack()

# Create a frame to hold the geometry-specific inputs
geometry_frame = tk.Frame(root)
geometry_frame.pack(pady=10)

# Place the labels and entries in the frame
label_radius = tk.Label(geometry_frame, text="Radius:")
entry_radius = tk.Entry(geometry_frame)

label_height = tk.Label(geometry_frame, text="Height:")
entry_height = tk.Entry(geometry_frame)

label_length = tk.Label(geometry_frame, text="Length:")
entry_length = tk.Entry(geometry_frame)

label_width = tk.Label(geometry_frame, text="Width:")
entry_width = tk.Entry(geometry_frame)

# Buttons to calculate volume and surface area
calculate_volume_button = tk.Button(geometry_frame, text="Calculate Volume", command=calculate_cuboid_volume)
calculate_volume_button.grid(row=4, column=0, columnspan=2, pady=5)

calculate_surface_area_button = tk.Button(geometry_frame, text="Calculate Surface Area", command=calculate_cuboid_surface_area)
calculate_surface_area_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
