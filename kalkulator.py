import math
import tkinter as tk
from tkinter import messagebox

# Constants
pi = 3.14159265359  # Use the precise value of pi

class PrismCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Prism Calculator")
        self.root.geometry("400x300")

        self.prism_types = ["Cylinder", "Cone", "Sphere", "Cuboid"]
        self.selected_prism = tk.StringVar()
        self.selected_prism.set(self.prism_types[0])
        self.selected_prism.trace("w", self.update_input_fields)

        self.create_widgets()
        self.update_input_fields()

    def create_widgets(self):
        tk.Label(self.root, text="Prism Type:").pack()

        tk.OptionMenu(self.root, self.selected_prism, *self.prism_types).pack()

        self.geometry_frame = tk.Frame(self.root)
        self.geometry_frame.pack(pady=10)

        self.label_radius = tk.Label(self.geometry_frame, text="Radius:")
        self.entry_radius = tk.Entry(self.geometry_frame)
        self.label_radius.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        self.entry_radius.grid(row=0, column=1, padx=5, pady=2)

        self.label_height = tk.Label(self.geometry_frame, text="Height:")
        self.entry_height = tk.Entry(self.geometry_frame)

        tk.Button(self.geometry_frame, text="Calculate Volume", command=self.calculate_volume).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(self.geometry_frame, text="Calculate Surface Area", command=self.calculate_surface_area).grid(row=3, column=0, columnspan=2, pady=5)

    def calculate_volume(self):
        r = float(self.entry_radius.get())
        h = float(self.entry_height.get())
        geometry = self.selected_prism.get()

        if geometry == "Cylinder":
            result = pi * r**2 * h
        elif geometry == "Cone":
            result = pi * r ** 2 * h / 3
        elif geometry == "Sphere":
            result = (4.0/3.0) * pi * r**3
        elif geometry == "Cuboid":
            l = float(self.entry_length.get())
            w = float(self.entry_width.get())
            result = l * w * h

        messagebox.showinfo(f"Volume of {geometry}", f"The volume is {result:.2f}")

    def calculate_surface_area(self):
        r = float(self.entry_radius.get())
        h = float(self.entry_height.get())
        geometry = self.selected_prism.get()

        if geometry == "Cylinder":
            result = 2 * pi * r * (r + h)
        elif geometry == "Cone":
            result = pi * r * (r + math.sqrt(r**2 + h**2))
        elif geometry == "Sphere":
            result = 4 * pi * r**2
        elif geometry == "Cuboid":
            l = float(self.entry_length.get())
            w = float(self.entry_width.get())
            result = 2 * (l*w + l*h + w*h)

        messagebox.showinfo(f"Surface Area of {geometry}", f"The surface area is {result:.2f}")

    def update_input_fields(self, *args):
        geometry = self.selected_prism.get()
        self.label_height.grid_forget()
        self.entry_height.grid_forget()

        if geometry != "Sphere":
            self.label_height.grid(row=1, column=0, padx=5, pady=2, sticky=tk.E)
            self.entry_height.grid(row=1, column=1, padx=5, pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = PrismCalculator(root)
    root.mainloop()





