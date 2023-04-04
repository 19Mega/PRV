from tkinter import *
from PIL import ImageTk, Image
import os.path

class PolygonEditor:
    def __init__(self, master, image_path):
        # Verifica que la imagen existe
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"La imagen {image_path} no existe.")

        # Carga la imagen
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Crea la ventana y el objeto Canvas
        self.master = master
        self.canvas = Canvas(master, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        # Muestra la imagen
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        # Crea una lista de vértices vacía
        self.vertices = []

        # Asocia el evento de clic del ratón a una función
        self.canvas.bind('<Button-1>', self.add_vertex)

    def add_vertex(self, event):
        # Si es el primer vértice del polígono, agrégalo y crea el polígono
        if len(self.vertices) == 0:
            self.vertices.append((event.x, event.y))
            self.polygon = self.canvas.create_polygon(self.vertices, outline='red', fill='')
        # De lo contrario, agrega un nuevo vértice al polígono
        else:
            self.vertices.append((event.x, event.y))
            # Actualiza las coordenadas del polígono
            self.canvas.coords(self.polygon, *[coord for vertex in self.vertices for coord in vertex])


# Crea la ventana principal
root = Tk()
root.title("Editor de polígonos")

# Crea una instancia del editor de polígonos
editor = PolygonEditor(root, "02Git/captura.jpg")

# Inicia el bucle principal de eventos
root.mainloop()
