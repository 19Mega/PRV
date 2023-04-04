from tkinter import *
from PIL import ImageTk, Image
import json
import os

# Crea la ventana principal
root = Tk()


# Fija el tamaño de la ventana principal
root.geometry("800x700")
root.resizable(False, False)


# Crea una etiqueta en la ventana para mostrar la imagen
image_label = Label(root, width=500)

# Abre la imagen y conviértela en un objeto de imagen tkinter
image = Image.open("02Git/captura.jpg")
tk_image = ImageTk.PhotoImage(image)

# Configura la etiqueta para mostrar la imagen
image_label.config(image=tk_image)
image_label.pack(side=RIGHT)

# Crea una barra lateral con 10 botones
button_frame = Frame(root, width=550)

# Chequea si el archivo json existe y si no, lo crea
if not os.path.exists("data.json"):
    data = {
        "1": {"fecha": "01/01/2023"},
        "2": {"fecha": "02/01/2023"},
        "3": {"fecha": "03/01/2023"},
        "4": {"fecha": "04/01/2023"},
        "5": {"fecha": "05/01/2023"},
        "6": {"fecha": "06/01/2023"},
        "7": {"fecha": "07/01/2023"},
        "8": {"fecha": "08/01/2023"},
        "9": {"fecha": "09/01/2023"},
        "10": {"fecha": "10/01/2023"}
    }
    with open("prv.json", "w") as file:
        json.dump(data, file, indent=2)

# Carga los datos del archivo json
with open("prv.json", "r") as file:
    datos = json.load(file)

# Crea los botones con los datos del archivo json
for i in range(1, 11):
    frame = Frame(button_frame, bd=1, relief=SOLID)
    frame.pack(side=TOP, fill=X)
    
    button_style = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "width": 15, "height": 2}
    button = Button(frame, text="Botón {}".format(i), **button_style)
    button.pack(side=LEFT, fill=X)
    
    label_style = {"font": ("Arial", 12), "bg": "#FFFFFF", "fg": "#555555", "width": 15, "height": 2}
    label = Label(frame, text="{}".format(datos[str(i)]["fecha"]), **label_style)
    label.pack(side=LEFT, fill=X)




button_frame.pack(side=LEFT, fill=Y)

# Ejecuta el bucle de eventos principal de tkinter
root.mainloop()


