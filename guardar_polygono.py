from tkinter import *
from PIL import ImageTk, Image
import os.path
import json

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

        # Crea una lista de polígonos vacía
        self.polygons = []

    def add_vertex(self, event):
        # Si es el primer vértice del polígono, agrégalo y crea el polígono
        if len(self.vertices) == 0:
            self.vertices.append((event.x, event.y))
            self.polygon = self.canvas.create_polygon(self.vertices, outline='white', fill='')
        # De lo contrario, agrega un nuevo vértice al polígono
        else:
            self.vertices.append((event.x, event.y))
            # Actualiza las coordenadas del polígono
            self.canvas.coords(self.polygon, *[coord for vertex in self.vertices for coord in vertex])

    def save_polygon(self):
        # Agrega el polígono actual a la lista de polígonos
        self.polygons.append(self.vertices)

        # Abre el archivo json en modo de escritura
        with open('polygons.json', 'w') as f:
            # Escribe la lista de polígonos en el archivo json
            json.dump(self.polygons, f)

    def load_polygons(self):
        # Abre el archivo json en modo de lectura
        try:
            with open('polygons.json', 'r') as f:
                # Carga la lista de polígonos del archivo json
                content = f.read().strip()
                if content:
                    self.polygons = json.loads(content)
                else:
                    self.polygons = []
        except FileNotFoundError:
            self.polygons = []

        # Dibuja cada polígono en el canvas
        for vertices in self.polygons:
            self.canvas.create_polygon(vertices, outline='white', fill='')

# Crea la ventana principal
root = Tk()
root.title("Editor de polígonos")

# Crea una instancia del editor de polígonos
editor = PolygonEditor(root, "02Git/captura.jpg")

# Crea el botón para guardar el polígono
save_button = Button(root, text="Guardar polígono", command=editor.save_polygon)
save_button.pack()

# Crea el botón para cargar los polígonos guardados
load_button = Button(root, text="Cargar polígonos", command=editor.load_polygons)
load_button.pack()

root.mainloop()

