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
# AREA ✔️ 
# ESPECIES

import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json
from datetime import datetime, date

class CalendarApp:
    def __init__(self):

        self.root = tk.Tk()
        self.root.config(bg="#312f47")

        # Crea y carga todos los datos del programa
        self.dates = []
        self.numbers = []
        self.lines = []

        # Contador para los potreros (numero antes de la fecha)
        self.counter = 0
        self.load_data()

        # self.rest_days()
        # self.use_time()

        self.create_calendar()

        #Frames
        self.campo_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.fecha_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.en_uso_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.descripcion_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.tamano_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.dias_descanso_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)
        self.tiempo_activo_frame = tk.Frame(self.root, bg="#312f47", relief="solid", bd=1)


        #Modificar tamaño y ancho de los frames y botones
        self.campo_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.fecha_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.en_uso_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.descripcion_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.tamano_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.dias_descanso_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)
        self.tiempo_activo_frame.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        #Labels
        campo_label = tk.Label(self.campo_frame, text="Potrero: ", anchor="nw", fg="white", bg="#2d4059", font=("Arial", 10, "bold"))
        fecha_label = tk.Label(self.fecha_frame, text="Ultimo Pastoreo: ", anchor="nw", fg="white", bg="#ea5455", font=("Arial", 10, "bold"))
        en_uso_label = tk.Label(self.en_uso_frame, text="En Uso: ", anchor="nw", fg="white", bg="#f07b3f", font=("Arial", 10, "bold"))
        descripcion_label = tk.Label(self.descripcion_frame, text="Descripción del Potrero: ", anchor="nw", fg="white", bg="#20bf6b", font=("Arial", 10, "bold"))
        tamano_label = tk.Label(self.tamano_frame, text="Tamaño: ", anchor="nw", fg="white", bg="#6d87a6", font=("Arial", 10, "bold"))
        dias_descanso_label = tk.Label(self.dias_descanso_frame, text="Días Descanso: ", anchor="nw", fg="black", bg="white", font=("Arial", 10, "bold"))
        tiempo_activo_label = tk.Label(self.tiempo_activo_frame, text="Tiempo: ", anchor="nw", fg="black", bg="white", font=("Arial", 10, "bold"))

        campo_label.pack(side="top", pady=5)
        fecha_label.pack(side="top", pady=5)
        en_uso_label.pack(side="top", pady=5)
        descripcion_label.pack(side="top", pady=5)
        tamano_label.pack(side="top", pady=5)
        dias_descanso_label.pack(side="top", pady=5)
        tiempo_activo_label.pack(side="top", pady=5)

    def create_calendar(self):
        self.cal = Calendar(self.root, selectmode='day')
        self.cal.pack(padx=10, pady=10)

        btn = tk.Button(self.root, text="Seleccionar fecha", command=self.create_selected_date, width=20)
        btn.pack(pady=10)

        btn_2 = tk.Button(self.root, text="Eliminar fecha", command=self.delete_last_date, width=20)
        btn_2.pack(pady=10)

    def create_selected_date(self):
        selected_date = self.cal.get_date()

        # Incrementar el contador y usar su valor como el identificador
        self.counter += 1
        potrero = self.counter

        is_active = False
        time_active = None
        description = "Descripcion del potrero"
        species = {} # pendiente
        area = "1 Ha"
        rest_days = str(self.calcule_rest_day(selected_date))

        self.dates.append((potrero, selected_date, description, area))
        print(f"Lista de fechas: {self.dates}")

        # numero potrer / dias descanso list

        campo_dato = tk.Button(self.campo_frame, text=potrero, anchor="center", command=self.print_hola, width=5, height=1)
        campo_dato.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        fecha_dato = tk.Label(self.fecha_frame, text=selected_date, anchor="nw")
        fecha_dato.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        en_uso_dato = tk.Label(self.en_uso_frame, text="Sí" if is_active else "No", anchor="nw")
        en_uso_dato.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        descripcion_dato = tk.Label(self.descripcion_frame, text=description, anchor="nw")
        descripcion_dato.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        tamano_dato = tk.Label(self.tamano_frame, text=area, anchor="nw")
        tamano_dato.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        dias_descanso = tk.Label(self.dias_descanso_frame, text=rest_days, anchor="nw")
        dias_descanso.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        tiempo_activo = tk.Label(self.tiempo_activo_frame, text="00:00:00", anchor="nw")
        tiempo_activo.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        self.save_data()

    def print_hola(self):
        print("Hola")

    def delete_last_date(self):
        self.dates.pop(-1)
        self.counter -= 1

        try:
            if self.counter >= 0 :
            # Elimina los widgets correspondientes 
                self.campo_frame.winfo_children()[-1].destroy()
                self.fecha_frame.winfo_children()[-1].destroy()
                self.en_uso_frame.winfo_children()[-1].destroy()
                self.descripcion_frame.winfo_children()[-1].destroy()
                self.tamano_frame.winfo_children()[-1].destroy()
                self.dias_descanso_frame.winfo_children()[-1].destroy()
                self.tiempo_activo_frame.winfo_children()[-1].destroy()
        except:
            pass

        print(f"lista dates: {self.dates}")
        self.save_data()

    # cronometro
    def use_time(self):
        for item in self.dates:
            if item[2] == True:
                print(f"Potrero usado: {item} ")

    def calcule_rest_day(self, fecha):
        selected_date = datetime.strptime(fecha, "%d/%m/%y").date()
        hoy = date.today()
        rest_day = hoy - selected_date
        print(f"HOLA AMIGOS ESTE ES EL DESCANSO: {rest_day.days}")
        return rest_day.days

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
            json.dump(data, f, indent=4)

app = CalendarApp()
app.root.mainloop()