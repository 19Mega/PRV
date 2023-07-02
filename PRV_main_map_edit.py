import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import json

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.main_color = "#C6D8C2"
        self.boton_color = "#F0F3ED"
        
        self.master = master
        self.pack()
        
        self.master.configure(bg=self.main_color)
        self.create_widgets() 

        self.next_number = 1
        self.number_positions = []

        self.line = None
        self.lines = []
        self.load_data()
        

        # hasta aca ejecuta cuando creamos un objeto del tipo app
        # despues tiene las funciones que se actival al interactuar con la ventana


    def create_widgets(self):
        # Coloca la ruta de la imagen manualmente
        image_path = "02Git/captura.jpg"

        # Carga la imagen con PIL y la convierte para poder mostrarla en el canvas
        self.image = Image.open(image_path)
        self.photo_image = ImageTk.PhotoImage(self.image)

        # Crea un canvas del mismo tamaño que la imagen
        self.canvas = tk.Canvas(self, width=self.image.width, height=self.image.height, bg= self.main_color)
        self.canvas.pack()

        # Pinta la imagen en el canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # Crea botones para las dos opciones
        self.line_button = tk.Button(self, text="Dibujar linea", command=self.set_mode_line, background=self.boton_color)
        self.number_button = tk.Button(self, text="Colocar numero", command=self.set_mode_number, background=self.boton_color)
        self.line_button.pack(side="left")
        self.number_button.pack(side="left")

        self.borrar_numeros_button = tk.Button(self, text="Borrar numeros", command=self.borrar_numeros, background=self.boton_color)
        self.borrar_numeros_button.pack(side="left")

        self.borrar_lines_button = tk.Button(self, text="Borrar lineas", command=self.borrar_lines, background=self.boton_color)
        self.borrar_lines_button.pack(side="left")

        # Vincula eventos del mouse en el canvas
        self.canvas.bind("<Button-1>", self.canvas_left_click) # 
        self.canvas.bind("<ButtonRelease-1>", self.canvas_left_release)
        self.canvas.bind("<B1-Motion>", self.canvas_left_drag)

    def set_mode_line(self):
        self.mode = "line"
        self.line_button.config(relief=tk.SUNKEN) # el boton queda apretado
        self.number_button.config(relief=tk.RAISED) # boton levantado

    def set_mode_number(self):
        self.mode = "number"
        self.line_button.config(relief=tk.RAISED) # boton queda levantado
        self.number_button.config(relief=tk.SUNKEN) # queda apretado


    #self.canvas.bind("<Button-1>", self.canvas_left_click) 
    def canvas_left_click(self, event):
        # Si se ha pulsado el boton de colocar numero
        if self.mode == "number":
            # Obtiene las coordenadas del clic
            x, y = event.x, event.y
            draw = ImageDraw.Draw(self.image) # crea objeto que vamos a colocar sobre la imagen

            #draw.text((x,y),)
            # Crea un nuevo numero con el valor incremental
            draw.text((x, y), str(self.next_number), fill='white') # le decimos al objeto que va ser un text
            self.number_positions.append((x, y))

            # Dibuja el numero en la capa "numbers"
                                #   ubicacion, texto, color, tag del archivo json
            self.canvas.create_text(x, y, text=str(self.next_number), fill='white', tags="numbers", font=("Arial", 15))
            
            #test
            total_de_numeros = len(self.number_positions)
            print(total_de_numeros)
            print(self.number_positions)

            self.next_number += 1

            # Guarda los datos
            self.save_data()

        # Si se ha pulsado el boton de dibujar linea
        elif self.mode == "line":
            # Obtiene las coordenadas del clic
            self.start_x, self.start_y = event.x, event.y


    def canvas_left_release(self, event):
        if self.mode == "line":

            x, y = event.x, event.y
            draw = ImageDraw.Draw(self.image)

            if self.line:
                self.canvas.delete(self.line)

            new_line = [(self.start_x, self.start_y), (x, y)]
            self.line = self.canvas.create_line(new_line, fill='white', width=3, tags="lines")

            self.lines.append(new_line)


            self.save_data()

    def canvas_left_drag(self, event):
        if self.mode == "line":
            x, y = event.x, event.y

            # Si ya habia una linea, la borra
            if self.line:
                self.canvas.delete("temp_line")

            # Dibuja una nueva linea temporal de 10px en las coordenadas del clic y el drag
            temp_line = [(self.start_x, self.start_y), (x, y)]
            self.line = self.canvas.create_line(temp_line, fill='skyblue', width=3, tags=("lines", "temp_line"))


    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

                self.number_positions = data["numbers"]

                self.lines = data["lines"]
                self.next_number = len(self.number_positions)+1

                # Dibuja los numeros previamente guardados en la capa "numbers"
                self.canvas.create_text(0, 0, text="", tags="numbers", font=("Arial", 15))

                # ACA AGREGA LOS NUMEROS, HAY QUE PINTAR UNO DE ROJO
                numero_potrero = 1
                for pos, i in zip(self.number_positions, range(self.next_number, len(self.number_positions)+self.next_number)):
                    self.canvas.create_text(pos[0], pos[1], text=str(numero_potrero), fill='white', tags="numbers", font=("Arial", 15))
                    numero_potrero +=1

                # Dibuja las li­neas previamente guardados en la capa "lines"
                self.canvas.create_line(0, 0, 0, 0, fill='white', width=3, tags="lines")
                for line in self.lines:
                    self.canvas.create_line(line, fill='white', width=3, tags="lines")

        except FileNotFoundError:
            pass

    def save_data(self):
        data = {
            "numbers": self.number_positions,
            "lines": self.lines
        }

        with open("data.json", "w") as f:
            json.dump(data, f)


    def borrar_numeros(self):
        self.canvas.delete("numbers")
        self.number_positions = []

        with open("data.json", "r") as f:
            data = json.load(f)

        data["numbers"] = []

        with open("data.json", "w") as f:
            json.dump(data, f)

        self.next_number = 1

    def borrar_lines(self):
        self.canvas.delete("lines")
        self.lines = []

        with open("data.json", "r") as f:
            data = json.load(f)

        data["lines"] = []

        with open("data.json", "w") as f:
            json.dump(data, f)
            



    # if __name__ == '__main__':
#root = tk.Tk()
#app = App(root)
# app.mainloop()


