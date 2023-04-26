import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json

# para el calculo de los descansos
from datetime import datetime, date


# HAY QUE HACER QUE EL MAPA CARGUE LAS DATES, PORQUE SINO ME LAS ELIMINA CUANDO ARRANCA A AGREGAR COSAS, HAY QUE METER EL DATES ALLA
# EN PRV_main_map_edit.py


#    TODO    #
# N° POTRERO ✔️
# FECHA ✔️
# DIAS DE DESCANSO ✔️ (no se guarda, se calcula y se muestra)

# IS ACTIVE? ✔️
# TIME ACTIVE
# TIME ACTIVE HISTORY 


# DESCRIPTION ✔️ 
# AREA 
# ESPECIES

class CalendarApp:
    def __init__(self):
        
        # Crea y carga todos los datos del programa
        self.dates = []
        self.numbers = []
        self.lines = []
        
        # Contador para los potreros (numero antes de la fecha)
        self.counter = 0 
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
        
        print(f"fecha seleccionada: {selected_date}")
        
        # Incrementar el contador y usar su valor como el identificador
        self.counter += 1
        potrero = self.counter
        
        is_active = False
        time_active = None
        description = "Descripcion del potrero"
        species = {} # pendiente
        area = "1 Ha"
        
        
        self.dates.append((potrero, selected_date, is_active, time_active, description, area))
        print(f"Lista de fechas: {self.dates}")
        
        self.save_data()
        
        
        
    def delete_last_date(self):
        self.dates.pop(-1)
        self.counter -= 1
        print(f"lista dates: {self.dates}")
        self.save_data()

    def rest_days(self):
        
        date_list = [] # Output: ['3/4/23', '4/4/23', '5/4/23']
        for item in self.dates:
            date_list.append(item[1])
        
        date_format_list = [] # Output: [datetime.date(2023, 4, 3), datetime.date(2023, 4, 4), datetime.date(2023, 4, 5)]
        try:
            for item in date_list:
                fecha = datetime.strptime(item, "%d/%m/%y").date()
                date_format_list.append(fecha)
        except IndexError:
            print("no hay fecha")

        hoy = date.today()
        print(f"HOY : {hoy}")
        
        rest_list = [] # Output: [datetime.timedelta(days=22), datetime.timedelta(days=21), datetime.timedelta(days=20)]
        try: # si no hay fechas no funciona 
            for fecha in date_format_list:
                descanso = hoy - fecha
                rest_list.append(descanso)
        except IndexError:
            print("no hay fecha para restar")        
        
        
        dias_list = [rest.days for rest in rest_list] # Output: [22, 21, 20] 
        print(dias_list)
        # 
        # for i, dato in enumerate(self.dates): # self.dates Output: [[1, '3/4/23', 22], [2, '4/4/23', 21], [3, '5/4/23', 20]]
        #    dato.append(dias_list[i])
        #    
        # print(self.dates)



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