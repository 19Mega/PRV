
#          02Git/captura.jpg


import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        # Inicializa variables para hacer numeros incrementales
        self.next_number = 1
        self.number_positions = []

        # Inicializa variable para la linea que se esta dibujando
        self.line = None

    def create_widgets(self):
        # Coloca la ruta de la imagen manualmente
        image_path = "02Git/captura.jpg"

        # Carga la imagen con PIL y la convierte para poder mostrarla en el canvas
        self.image = Image.open(image_path)
        self.photo_image = ImageTk.PhotoImage(self.image)

        # Crea un canvas del mismo tamaño que la imagen
        self.canvas = tk.Canvas(self, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        # Pinta la imagen en el canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # Crea botones para las dos opciones
        self.line_button = tk.Button(self, text="Dibujar linea", command=self.set_mode_line)
        self.number_button = tk.Button(self, text="Colocar numero", command=self.set_mode_number)
        self.line_button.pack(side="left")
        self.number_button.pack(side="left")

        # Vincula eventos del mouse en el canvas
        self.canvas.bind("<Button-1>", self.canvas_left_click)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_left_release)
        self.canvas.bind("<B1-Motion>", self.canvas_left_drag)

    def set_mode_line(self):
        self.mode = "line"
        self.line_button.config(relief=tk.SUNKEN)
        self.number_button.config(relief=tk.RAISED)

    def set_mode_number(self):
        self.mode = "number"
        self.line_button.config(relief=tk.RAISED)
        self.number_button.config(relief=tk.SUNKEN)

    def canvas_left_click(self, event):
        # Si se ha pulsado el boton de colocar numero
        if self.mode == "number":
            # Obtiene las coordenadas del clic
            x, y = event.x, event.y
            draw = ImageDraw.Draw(self.image)

            # Crea un nuevo numero con el valor incremental
            draw.text((x, y), str(self.next_number), fill='white')
            self.next_number += 1
            self.number_positions.append((x, y))

            # Actualiza la imagen del canvas con los cambios
            self.photo_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # Si se ha pulsado el boton de dibujar linea
        elif self.mode == "line":
            # Obtiene las coordenadas del clic
            self.start_x, self.start_y = event.x, event.y

    def canvas_left_release(self, event):
            # Si se ha pulsado el boton de dibujar linea
            if self.mode == "line":
                # Obtiene las coordenadas del release
                x, y = event.x, event.y
                draw = ImageDraw.Draw(self.image)

                # Si ya habia una linea, la borra
                if self.line:
                    self.canvas.delete(self.line)

                # Dibuja una linea de 10px en las coordenadas del clic y release
                self.line = self.canvas.create_line(self.start_x, self.start_y, x, y, fill='white', width=3)

                # Dibuja la linea en la imagen usando ImageDraw
                draw.line([(self.start_x, self.start_y), (x, y)], fill='white', width=3)

                # Actualiza la imagen del canvas con los cambios
                self.photo_image = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)



    def canvas_left_drag(self, event):
        # Si se ha pulsado el boton de dibujar linea
        if self.mode == "line":
            # Obtiene las coordenadas del drag
            x, y = event.x, event.y

            # Si ya habia una linea, la borra
            if self.line:
                self.canvas.delete(self.line)

            # Dibuja una nueva linea de 10px en las coordenadas del clic y el drag
            self.line = self.canvas.create_line(self.start_x, self.start_y, x, y, fill='skyblue', width=3)

    def clear_canvas(self):
        # Borra todas las linea y numero del canvas y los listados internamente
        for position in self.number_positions:
            self.canvas.delete(position)
        self.number_positions = []
        self.canvas.delete(self.line)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()