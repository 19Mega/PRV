import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json

# para el calculo de los descansos
from datetime import datetime, date


# HAY QUE HACER QUE EL MAPA CARGUE LAS DATES, PORQUE SINO ME LAS ELIMINA CUANDO ARRANCA A AGREGAR COSAS, HAY QUE METER EL DATES ALLA
# EN PRV_main_map_edit.py

# NUMERO POTRERO ✔️ / FECHA ✔️ / DIAS DE DESCANSO / IS ACTIVE? / DESCRIPTION / AREA / ESPECIES

class CalendarApp:
    def __init__(self):
        
        # Crea y carga todos los datos del programa
        self.dates = []
        self.numbers = []
        self.lines = []
        
        # Contador para los potreros (numero antes de la fecha)
        self.counter = 0 
        self.load_data()  
        
        
        date_list = []
        for item in self.dates:
            date_list.append(item[1])
        print(date_list) 
        
        hoy = date.today()
        print(f"HOY : {hoy}")
        
        try:
            fecha = datetime.strptime(date_list[0], "%d/%m/%y").date()
            print(f"FECHA: {fecha}")
        except IndexError:
            print("no hay fecha")
        
        # si no hay fechas no funciona 
        aca = hoy.day - fecha.day
        print(aca)
        
        '''
        hoy = date.today()
        fecha_formateada = hoy.strftime("%d/%m/%Y")
        print(f"HOY : {fecha_formateada}") # output: HOY : 24/4/2023
        
        resta = int(fecha_formateada) - int(date_list[0])
        
        print(f"RESTA : {resta}")
        
        ###############
        
        # transforma str en fecha 
    
        fecha = datetime.strptime(date_list[0], "%d/%m/%y").date()
        print(f"FECHA: {fecha}")
        
        '''
        
        
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
        
        print(f"fecha seleccionada: {selected_date}")
        
        
        
        
        
        # Incrementar el contador y usar su valor como el identificador
        self.counter += 1
        potrero = self.counter
        
        self.dates.append((potrero, selected_date))
        print(f"Lista de fechas: {self.dates}")
        self.save_data()
        
    def delete_last_date(self):
        self.dates.pop(-1)
        self.counter -= 1
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
            
        # Tomamos el ultimo numero de fecha que haya
        try:
            last_date = self.dates[-1]
            self.counter = last_date[0]
            print(self.counter)
        except IndexError:
            print("La lista de fechas está vacía.")
            self.counter = 0

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