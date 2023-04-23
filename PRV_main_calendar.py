import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json

# HAY QUE HACER QUE EL MAPA CARGUE LAS DATES, PORQUE SINO ME LAS ELIMINA CUANDO ARRANCA A AGREGAR COSAS, HAY QUE METER EL DATES ALLA
# EN PRV_main_map_edit.py

class CalendarApp:
    def __init__(self):
        
        # Crea y carga todos los datos del programa
        self.dates = []
        self.numbers = []
        self.lines = []
        self.load_data()
        
        
        self.create_calendar()
        
        
    def create_calendar(self):
        self.root = tk.Tk()

        self.cal = Calendar(self.root, selectmode='day')
        self.cal.pack(padx=10, pady=10)

        btn = tk.Button(self.root, text="Seleccionar fecha", command=self.create_selected_date)
        btn.pack(pady=10)
        
        btn_2 = tk.Button(self.root, text="Eliminar fecha", command=self.delete_last_date)
        btn_2.pack(pady=10)
        

    def create_selected_date(self):
        selected_date = self.cal.get_date()
        print(selected_date)
        self.dates.append(self.cal.get_date())
        print(f"lista fechas: {self.dates}")
        
        self.save_data()
        
    def delete_last_date(self):
        self.dates.pop(-1)
        print(f"lista dates: {self.dates}")
        self.save_data()


    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                self.numbers = data["numbers"]
                self.lines = data["lines"]
                # despues de agregar dates a el editor de map, revisamos aca ! ! ! ! !
                try:
                    self.dates = data["dates"]
                except KeyError:
                    self.dates = []
        except FileNotFoundError:
            print("El archivo de datos 'data.json' no existe. Se creará uno nuevo con 3 listas vacías.")
            self.numbers = []
            self.lines = []
            self.dates = []
            self.save_data()

    def save_data(self):
        data = {
            "dates": self.dates,
            "numbers": self.numbers,
            "lines": self.lines
        }
        with open("data.json", "w") as f:
            json.dump(data, f)



app = CalendarApp()
app.root.mainloop()