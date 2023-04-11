from tkinter import *
from PIL import ImageTk, Image
import os.path
import json

class Vertice:
    def __init__(self, canvas):
        self.canvas = canvas
        # modos edit, no_edit
        self.mode = "no_edit"  # Modo de edición/agregado (por defecto, agregado)
        self.number_mode = "no_number"
        
        # lines
        self.x, self.y = None, None
        self.line = None
        
        # lines
        self.state_button = "OFF"
        self.mode_button = Button(root, text=f"Editor de Potreros: ", command=self.toggle_line_mode)
        self.mode_button.pack()
        self.save_button = Button(root, text="Guardar", command=self.save_lines)
        self.save_button.pack()
        
        # number
        #self.state_number_button = "OFF"
        #self.mode_number_button = Button(root, text=f"Editor de Numeros: ", command=self.toggle_number_mode)
        #self.mode_number_button.pack()
        
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_line)
        self.canvas.bind("<Button-3>", self.delete_line)
        
        
        
        # numbers
        self.count = 0
        self.adding_numbers = False
        self.numbers = []
        self.load_numbers()
        for x, y, number in self.numbers:
            self.count += 1
            self.canvas.create_text(x, y, text=number, fill="white", font=("Arial", 14))
        
        
        
        #self.load_button = Button(root, text="Cargar", command=self.load_lines)
        #self.load_button.pack()
        self.load_lines()


    # numbers
    def load_numbers(self):
        if os.path.isfile("numbers.json"):
            with open("numbers.json", "r") as f:
                self.numbers = json.load(f)


    # lines
    def start_line(self, event):
        if self.mode == "edit":
            self.x, self.y = event.x, event.y
            self.line = self.canvas.create_line(self.x, self.y, self.x, self.y, width=3, fill='white')

    def draw_line(self, event):
        if self.mode == "edit" and self.x and self.y:
            self.canvas.coords(self.line, self.x, self.y, event.x, event.y)

    def stop_line(self, event):
        if self.mode == "edit":
            self.x, self.y = None, None
            self.line = None

    def save_lines(self):
        lines = []
        for item in self.canvas.find_all():
            if self.canvas.type(item) == "line":
                coords = self.canvas.coords(item)
                lines.append((coords[0], coords[1], coords[2], coords[3]))
        with open("lines.json", "w") as f:
            json.dump(lines, f)

    def load_lines(self):
        if os.path.exists("lines.json"):
            with open("lines.json", "r") as f:
                lines = json.load(f)
            for coords in lines:
                self.canvas.create_line(coords[0], coords[1], coords[2], coords[3], width=3, fill='white')

    def delete_line(self, event):
        if self.mode == "edit":
            item = self.canvas.find_closest(event.x, event.y)[0]
            if self.canvas.type(item) == "line":
                self.canvas.delete(item)

    def toggle_line_mode(self):
        if self.mode == "edit":
            self.mode = "no_edit"
            self.state_button = "OFF"
            self.mode_button.configure(bg='gray20', fg='white')   
        else:
            self.mode = "edit"
            self.state_button = "ON"
            self.mode_button.configure(bg='green', fg='white')
        self.mode_button.config(text=f"Editor de Potreros: {self.state_button}")


    # number
    def toggle_number_mode(self):
        if self.number_mode == "number":
            self.number_mode = "no_number"
            self.state_number_button = "OFF"
            self.mode_number_button.configure(bg='gray20', fg='white')
        else:
            self.number_mode = "number"
            self.state_number_button = "ON"
            self.mode_number_button.configure(bg='green', fg='white')
        self.mode_number_button.config(text=f"Editor de Potreros: {self.state_number_button}")


root = Tk()
root.geometry("440x750")
canvas = Canvas(root, width=450, height=650)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("02Git/captura.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

v = Vertice(canvas)

root.mainloop()