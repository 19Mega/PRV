from tkinter import *
from PIL import ImageTk, Image
import os.path
import json

root = Tk()
canvas = Canvas(root, width=800, height=700)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("02Git/captura.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

mode = "no_edit"  # Modo de edición/agregado (por defecto, agregado)

x, y = None, None
line = None

def start_line(event):
    global x, y, line
    if mode == "edit":
        x, y = event.x, event.y
        line = canvas.create_line(x, y, x, y, width=3, fill='white')

def draw_line(event):
    global x, y, line
    if mode == "edit" and x and y:
        canvas.coords(line, x, y, event.x, event.y)

def stop_line(event):
    global x, y, line
    if mode == "edit":
        x, y = None, None
        line = None

def save_lines():
    lines = []
    for item in canvas.find_all():
        if canvas.type(item) == "line":
            coords = canvas.coords(item)
            lines.append((coords[0], coords[1], coords[2], coords[3]))
    with open("lines.json", "w") as f:
        json.dump(lines, f)

def load_lines():
    if os.path.exists("lines.json"):
        with open("lines.json", "r") as f:
            lines = json.load(f)
        for coords in lines:
            canvas.create_line(coords[0], coords[1], coords[2], coords[3], width=3, fill='white')

load_lines()

def delete_line(event):
    if mode == "edit":
        item = canvas.find_closest(event.x, event.y)[0]
        if canvas.type(item) == "line":
            canvas.delete(item)


canvas.bind("<Button-1>", start_line)
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", stop_line)
canvas.bind("<Button-3>", delete_line)

state_button = "OFF"

def toggle_mode():
    global mode, state_button
    if mode == "edit":
        mode = "no_edit"
        state_button = "OFF"
        mode_button.configure(bg='gray20', fg='white')
    else:
        mode = "edit"
        state_button = "ON"
        mode_button.configure(bg='green', fg='white')
    mode_button.config(text=f"Editor de Potreros: {state_button}")




mode_button = Button(root, text=f"Editor de Potreros: ", command=toggle_mode)
mode_button.pack()

save_button = Button(root, text="Guardar", command=save_lines)
save_button.pack()

load_button = Button(root, text="Cargar", command=load_lines)
load_button.pack()



root.mainloop()
