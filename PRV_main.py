from tkinter import *
from PIL import ImageTk, Image
import json
import os

root = Tk()
root.geometry("700x750")
root.resizable(False, False)
root.configure(borderwidth=15, highlightthickness=10)

image_label = Label(root, width=450)

image = Image.open("02Git/captura.jpg")
tk_image = ImageTk.PhotoImage(image)

image_label.config(image=tk_image)
image_label.pack(side=RIGHT)

title_label = Label(root, text="Potreros", font=("Arial", 14), pady=5)
title_label.pack()

button_frame = Frame(root, width=100)

if not os.path.exists("data.json"):
    data = {
        "1": {"fecha": "01/01/2023"},
        "2": {"fecha": "02/01/2023"},
        "3": {"fecha": "03/01/2023"},
        "4": {"fecha": "04/01/2023"},
        "5": {"fecha": "05/01/2023"}
    }
    with open("prv.json", "w") as file:
        json.dump(data, file, indent=2)

with open("prv.json", "r") as file:
    datos = json.load(file)

for i in range(1, 6):
    frame = Frame(button_frame, bd=1, relief=SOLID)
    frame.pack(side=TOP, fill=X)
    
    button_style = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "width": 5, "height": 1}
    button = Button(frame, text=" {}".format(i), **button_style)
    button.pack(side=LEFT, fill=X)
    
    label_style = {"font": ("Arial", 12), "bg": "#FFFFFF", "fg": "#555555", "width": 10, "height": 1}
    label = Label(frame, text="{}".format(datos[str(i)]["fecha"]), **label_style)
    label.pack(side=LEFT, fill=X)

button_frame.pack(side=LEFT, fill=Y)

root.mainloop()



