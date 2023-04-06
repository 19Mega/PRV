from tkinter import *
from PIL import ImageTk, Image
import json
import os.path

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Agregar número a imagen")

        self.image_path = "02Git/captura.jpg"
        self.image = Image.open(self.image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(master, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)
        self.canvas.pack()

        self.undo_button = Button(master, text="Deshacer último número", command=self.undo_last_number, bg="dark gray")
        self.undo_button.pack(side=LEFT)

        self.count = 0
        self.adding_numbers = False
        self.numbers = []
        self.load_numbers()
        for x, y, number in self.numbers:
            self.count += 1
            self.canvas.create_text(x, y, text=number, fill="white")

        self.add_number_button = Button(master, text=f"Agregar número ({self.count})", command=self.toggle_adding_numbers, bg="dark gray")
        self.add_number_button.pack(side=LEFT)

        self.canvas.bind("<Button-1>", self.place_number)
        self.toggle_adding_numbers()

    def toggle_adding_numbers(self):
        self.adding_numbers = not self.adding_numbers
        if self.adding_numbers:
            self.add_number_button.config(text="Dejar de agregar números", bg="green")
        else:
            self.add_number_button.config(text=f"Agregar número ({self.count})", bg="dark gray")

    def place_number(self, event):
        if self.adding_numbers:
            number = str(self.count + 1)
            self.count += 1
            self.add_number_button.config(text=f"Agregar número ({self.count})", bg="green")
            self.canvas.create_text(event.x, event.y, text=number, fill="white")
            self.numbers.append((event.x, event.y, number))
            self.save_numbers()

    def save_numbers(self):
        with open("numbers.json", "w") as f:
            json.dump(self.numbers, f)

    def load_numbers(self):
        if os.path.isfile("numbers.json"):
            with open("numbers.json", "r") as f:
                self.numbers = json.load(f)

    def undo_last_number(self):
        if self.numbers:
            self.count -= 1
            self.numbers.pop()
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)
            for x, y, number in self.numbers:
                self.canvas.create_text(x, y, text=number, fill="white")
            self.add_number_button.config(text=f"Agregar número ({self.count})", bg="dark gray")
            self.save_numbers()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    app.run()