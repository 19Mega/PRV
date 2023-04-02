from tkinter import *
from PIL import ImageTk, Image

# Crea la ventana principal
root = Tk()

# Crea una etiqueta en la ventana para mostrar la imagen
image_label = Label(root)

# Abre la imagen y conviértela en un objeto de imagen tkinter
image = Image.open("02Git/captura.jpg")
tk_image = ImageTk.PhotoImage(image)

# Configura la etiqueta para mostrar la imagen
image_label.config(image=tk_image)
image_label.pack()

# Ejecuta el bucle de eventos principal de tkinter
root.mainloop()
