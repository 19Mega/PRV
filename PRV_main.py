import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

from PRV_main_map_edit import App
from PRV_sqlite_connection import Comunication

mi_comunicacion = Comunication()
mi_comunicacion.rest_days_update()

main_color = "#C6D8C2"
boton_color = "#F0F3ED"

# main_color = "#CCCFCD" ORIGINAL
#5F6F5B : Verde oscuro
#538C45 : Verde de botones
#312f47 : Azul oscuro antiguo

# ID, parcelNumber, parcelDescription, parcelSize, parcelSpecies, 
# parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime

class MyButton(Button):
    def __init__(self, master, 
                parcelNumber, 
                parcelDescription, 
                parcelSize,
                parcelSpecies,
                parcelStocking,
                parcelLastGrazingDate,
                restDays,
                isActive,
                grazinTime,
                *args, **kwargs):

        super().__init__(master, *args, **kwargs)
        self.parcelNumber = parcelNumber
        self.parcelDescription = parcelDescription
        self.parcelSize = parcelSize
        self.parcelSpecies = parcelSpecies
        self.parcelStocking = parcelStocking
        self.parcelLastGrazingDate = parcelLastGrazingDate
        self.restDays = restDays
        self.isActive = isActive
        self.grazinTime = grazinTime       


        self.new_date_format = self.date_format(self.parcelLastGrazingDate)
        
        
        fecha_str = mi_comunicacion.get_parcelLastGrazingDate(parcelNumber) # agarramos 
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S.%f')
        self.diferencia = datetime.now() - fecha

        '''
        self.config(text=f"N° {parcelNumber}\nDescanso: {restDays} Días\nEstado: {'Activo' if isActive else 'Inactivo'}",
                    width=14, height=3, font=("Arial", 8),
                    command=self.custom_callback)        
        '''

        if isActive: self.set_color_green()
        else: self.set_color_grey()
        
        
        


    # COLOR BOTON: VERDE/ACTIVO
    def set_color_green(self):
        #self.config(text=f"N° {self.parcelNumber}  Descanso: {self.restDays} Días\n{'Activo' if self.isActive else 'Inactivo'}",
        #    font=("Arial", 9), fg="white", background="#5E6DA9", width=20, height=2, command=self.custom_callback)
        
        self.config(text=f"N° {self.parcelNumber}  Descanso: 0 Días \n{'EN PASTOREO' if self.isActive else 'Inactivo'}",
            font=("Arial", 9), fg="white", background="#538C45", width=20, height=2, command=self.custom_callback)


    # COLOR BOTON: GRIS/inACTIVO
    def set_color_grey(self):
        self.config(text=f"N° {self.parcelNumber}  Descanso: {self.restDays} Días\n{'Activo' if self.isActive else 'Inactivo'}",
            font=("Arial", 9), fg="black", background="#D4D4D4", width=20, height=2, command=self.custom_callback)


    # FUNCIONES
    def calcular_diferencia(self):
        if self.isActive:
            fecha_str = mi_comunicacion.get_parcelLastGrazingDate(self.parcelNumber)
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S.%f')    
            self.diferencia = datetime.now() - fecha
            # self.label.config(text="{} días, {}:{:02d}".format(self.diferencia.days, self.diferencia.seconds // 3600, (self.diferencia.seconds // 60) % 60))
            self.grazin_time_label.config(text="{} días, {:02d}:{:02d}:{:02d}".format(self.diferencia.days, self.diferencia.seconds // 3600, (self.diferencia.seconds // 60) % 60, self.diferencia.seconds % 60))
            self.after(1000, self.calcular_diferencia)
        else:
            self.diferencia = None
            self.grazin_time_label.config(text="00:00:00")
            self.after(1000, self.calcular_diferencia)


    # PREGUNTA Empezar pastoreo
    def isActive_True(self):
        respuesta = messagebox.askquestion("Empezar pastoreo en potrero", "¿Desea comenzar el pastoreo ?")

        if respuesta == "yes":            
            if mi_comunicacion.get_isActive(self.parcelNumber) == False:
                # podria ir algo como para guardar el progreso que se tenia en descansos en algun historial

                # empezar a contar el reloj (esto lo hace solo la funcion calcular_diferencia())
                self.isActive = True
                mi_comunicacion.set_isActive(self.parcelNumber, self.isActive)
                self.is_active_label.config(text='Sí' if self.isActive else 'No')

                # actualiza parcelLastGrazingDate 
                mi_comunicacion.set_parcelLastGrazingDate(self.parcelNumber, datetime.now()) 
                self.parcelLastGrazingDate_label.config(text="Hoy, en pastoreo")

                # actualizar el rest days
                mi_comunicacion.rest_days_update()

                self.restDays_label.config(text=" - ")

                # actualiza boton de potreros
                self.set_color_green()


    # PREGUNTA Terminar pastoreo
    def isActive_False(self):
        respuesta = messagebox.askquestion("Terminar pastoreo en potrero", "¿Desea terminar el pastoreo?")
        if respuesta == "yes":            
            # actualizamos isActive
            self.isActive = False
            mi_comunicacion.set_isActive(self.parcelNumber, self.isActive) 
            self.is_active_label.config(text='Sí' if self.isActive else 'No')

            # actualiza parcelLastGrazingDate 
            mi_comunicacion.set_parcelLastGrazingDate(self.parcelNumber, datetime.now()) 
            self.parcelLastGrazingDate = mi_comunicacion.get_parcelLastGrazingDate(self.parcelNumber)            
            self.parcelLastGrazingDate_label.config(text=(self.new_date_format.day ,"/", self.new_date_format.month, "/",self.new_date_format.year))

            # actualizar el rest days
            mi_comunicacion.rest_days_update()
            self.restDays = mi_comunicacion.get_restDays(self.parcelNumber) 
            self.restDays_label.config(text=self.restDays)

            # actualiza boton de potreros
            self.set_color_grey()




    # Elimina todos los widgets dentro del frame2.
    def clear_frame2(self):
        for widget in frame2.winfo_children():
            widget.destroy()

    def date_format(self, parcelLastGrazingDate):
        format_fecha = datetime.strptime(parcelLastGrazingDate, '%Y-%m-%d %H:%M:%S.%f')    
        return(format_fecha.date())
    
    
    # ENTRYs: parcelDescription, parcelSpecies, parcelStocking, parcelSize
    def save_parcel_description(self):
        new_parceDescription = self.parcelDescription_text.get("1.0", tk.END)
        print("PRUEBA: ", new_parceDescription)
        self.parcelDescription = new_parceDescription
        mi_comunicacion.set_parcelDescription(self.parcelNumber, new_parceDescription)
    
    def save_parcel_species(self):
        new_parcelSpecies = self.parcelSpecies_text.get("1.0", tk.END)
        print("PRUEBA: ", new_parcelSpecies)
        self.parcelSpecies = new_parcelSpecies
        mi_comunicacion.set_parcelSpecies(self.parcelNumber, new_parcelSpecies)
        
    def save_parcel_stocking(self):
        new_parcelStocking = self.parcelStocking_text.get("1.0", tk.END)
        print("PRUEBA: ", new_parcelStocking)
        self.parcelStocking = new_parcelStocking
        mi_comunicacion.set_parcelStocking(self.parcelNumber, new_parcelStocking)
        # mi_comunicacion.set_parcelStockingForAll(self.parcelStocking) 
        # Funcion para actualizar todos, no actualiza los de los otros potreros, solo cuando se reinicia 
        
    def save_parcel_Size(self):
        new_parcelSize = self.parcelSize_text.get("1.0", tk.END)
        print("PRUEBA: ", new_parcelSize)
        self.parcelSize = new_parcelSize
        mi_comunicacion.set_parcelSize(self.parcelNumber, new_parcelSize)    
        

    # CREA LA SECCION DE INFO (cuando clicleamos un potrero)
    def custom_callback(self):
        self.clear_frame2()
        
        # TITULO ROW = 0
        Label(frame2, text="   Información del Pastoreo   ",relief="solid", font=("Arial", 22), anchor="e", bg=main_color).grid(row=0, column=0, columnspan=3, sticky="s", pady=15, padx=15)
        
        # LINEA DE ESPACIO - ANCHO IDEAL DE LA SECCION INFO: height=500 - ROW = 1
        # Label(frame2, height=0, width=70, bg=main_color).grid(row=1, column=0, columnspan=3, pady=0, padx=2)
        
        # parcelNumber title ROW = 2
        Label(frame2, text="Potrero N°:", font=("Arial", 12), anchor="e",  bg=main_color).grid(row=2, column=0, sticky=W, pady=2, padx=(0, 10))
        # parcelNumber ROW = 3
        Label(frame2, text=self.parcelNumber, font=("Arial", 20),relief="groove", anchor="center",height=1, bg=main_color).grid(row=3, column=0, sticky="nswe", pady=1, padx=(0, 5))
        # relief="solid" # borde
        
        # restDays ROW = 2 y ROW = 3
        Label(frame2, text="Días de Descanso:", font=("Arial", 12),  bg=main_color).grid(row=2, column=2, sticky=W, pady=2)
        self.restDays_label = Label(frame2, text=self.restDays, font=("Arial", 20),relief="groove", bg= main_color)
        self.restDays_label.grid(row=3, column=2, sticky=W, pady=2)
        
        # ROW = 4
        Label(frame2, height=1, width=70, bg=main_color).grid(row=4, column=0, columnspan=3, pady=0, padx=2)

        # parcelLastGrazingDate ROW = 5
        Label(frame2, text="Último Día de Pastoreo: ",font=("Arial", 12), bg=main_color).grid(row=5, column=0, sticky=W, pady=0)
        self.parcelLastGrazingDate_label = Label(frame2, text="Hoy, en pastoreo" if self.isActive else (self.new_date_format.day ,"/", self.new_date_format.month, "/",self.new_date_format.year), font=("Arial", 12), bg=main_color)
        self.parcelLastGrazingDate_label.grid(row=5, column=1, sticky=W, pady=2)

        # ROW = 6
        Label(frame2, height=1, width=70, bg=main_color).grid(row=6, column=0, columnspan=3, pady=0, padx=2)

        # isActive - ROW = 7
        Label(frame2, text="Potrero en pastoreo: ",font=("Arial", 12),  bg=main_color).grid(row=7, column=0, sticky=W, pady=2)
        self.is_active_label = Label(frame2, text='Sí' if self.isActive else 'No', font=("Arial", 12), bg=main_color)
        self.is_active_label.grid(row=7, column=1, sticky=W, pady=2)

        # BOTONES ROW = 7 y ROW = 8
        Button(frame2, text="Empezar pastoreo",font=("Arial", 10), command=self.isActive_True, background=boton_color).grid(row=7, column=2, sticky=W, pady=2)
        Button(frame2, text="Terminar pastoreo",font=("Arial", 10), command=self.isActive_False, background=boton_color).grid(row=8, column=2, sticky=W, pady=2)

        # Label(frame2, text="Tiempo de Pastoreo:").grid(row=8, column=0, sticky=W, pady=2)
        # Label(frame2, text=f"{self.diferencia} horas/día", relief="sunken").grid(row=8, column=1, sticky=W, pady=2)
        # Label(frame2, text=f"{self.diferencia} horas/día", relief="sunken", font=("Arial", 16), padx=10, pady=10).grid(row=8, column=1, sticky=W)

        Label(frame2, text="Tiempo de Pastoreo:", font=("Arial", 12),  bg=main_color).grid(row=8, column=0, sticky=W, pady=2)
        
        if self.diferencia is not None:
            self.grazin_time_label = Label(frame2, text="{} días, {}:{:02d}:{:02d}".format(self.diferencia.days, self.diferencia.seconds // 3600, (self.diferencia.seconds // 60) % 60, self.diferencia.seconds % 60), font=("Arial", 12), bg=main_color)
            self.grazin_time_label.grid(row=8, column=1, sticky=W, pady=2)
        else:   
            self.grazin_time_label = Label(frame2, text="00:00:00", font=("Arial", 12), bg=main_color)
            self.grazin_time_label.grid(row=8, column=1, sticky=W, pady=2)        
        
        self.calcular_diferencia()
        
        # ROW = 9
        Label(frame2, height=1, width=70, bg=main_color).grid(row=9, column=0, columnspan=3, pady=0, padx=2)
        
        # parcelStocking ROW = 10
        Label(frame2, text="Carga de animales: ", font=("Arial", 12), bg=main_color).grid(row=10, column=0, sticky=W, pady=2)
        
        self.parcelStocking_text = Text(frame2, font=("Arial", 12), width=5,height=1, wrap="word")
        self.parcelStocking_text.insert("1.0", self.parcelStocking)
        self.parcelStocking_text.grid(row=10, column=1, pady=2, sticky="w")
        
        Button(frame2, text="Guardar Lote",font=("Arial", 10), command= self.save_parcel_stocking, background=boton_color).grid(row=10, column=2, sticky=W, pady=2)
        
        # Label(frame2, text=self.parcelStocking, font=("Arial", 12)).grid(row=10, column=1, sticky=W, pady=2)
        
        # SUBTITLE ROW= 11
        Label(frame2, text="   Información del Potrero   ",relief="solid", font=("Arial", 22), anchor="e",  bg=main_color).grid(row=11, column=0, columnspan=3, sticky="s", pady=10, padx=10)
        
        # parcelSize ROW = 12
        Label(frame2, text="Tamaño en Ha: ", font=("Arial", 12),  bg=main_color).grid(row=12, column=0, sticky=W, pady=2)
        # Label(frame2, text=f"{self.parcelSize} Hectáreas", font=("Arial", 12)).grid(row=12, column=1, sticky=W, pady=2)
        
        self.parcelSize_text = Text(frame2, font=("Arial", 12), width=5,height=1, wrap="word")
        self.parcelSize_text.insert("1.0", self.parcelSize)
        self.parcelSize_text.grid(row=12, column=1, pady=2, sticky="w")
        
        Button(frame2, text="Guardar Tamaño",font=("Arial", 10), command= self.save_parcel_Size, background=boton_color).grid(row=12, column=2, sticky=W, pady=2)

        # parcelSpecies ROW = 13
        Label(frame2, text="Vegetación: " ,font=("Arial", 12), bg=main_color).grid(row=13, column=0, sticky=W, pady=2)
        # Label(frame2, text=self.parcelSpecies, font=("Arial", 12)).grid(row=13, column=1, sticky=W, pady=2)
        
        self.parcelSpecies_text = Text(frame2, font=("Arial", 12), width=54,height=4, wrap="word")
        self.parcelSpecies_text.insert("1.0", self.parcelSpecies)
        self.parcelSpecies_text.grid(row=14, column=0, columnspan=3, pady=2)
        
        Button(frame2, text="Guardar Vegetación",font=("Arial", 10), command= self.save_parcel_species, background=boton_color).grid(row=13, column=2, sticky=W, pady=2)
        
        Label(frame2, height=0, width=70, bg=main_color).grid(row=15, column=0, columnspan=3, pady=1, padx=2)
        
        # parcelDescription ROW = 15 y 16
        Label(frame2, text="Descripción: ", font=("Arial", 12),  bg=main_color).grid(row=16, column=0, sticky=W, pady=2)
        # Entry(frame2, text=self.parcelDescription, font=("Arial", 12), width=54).grid(row=16, column=0, columnspan=3, pady=2)
        # parcelDescription_label = 
        self.parcelDescription_text = Text(frame2, font=("Arial", 12), width=54,height=4, wrap="word")
        self.parcelDescription_text.insert("1.0", self.parcelDescription)
        self.parcelDescription_text.grid(row=17, column=0, columnspan=3, pady=2)
        
        Button(frame2, text="Guardar Descripción",font=("Arial", 10), command= self.save_parcel_description,background=boton_color).grid(row=16, column=2, sticky=W, pady=2)

        
        # LINEA DE ESPACIO GRUESA
        Label(frame2, height=2, width=0,bg=main_color).grid(row=18, column=0, columnspan=3, pady=0)

        # para poner " - " en restDays
        if self.isActive : self.restDays_label.config(text=" - ")







# Crear instancia de Tkinter
root = tk.Tk()


# Crear los tres frames (secciones verticales)
frame1 = tk.Frame(root, bg=main_color)
frame_buttons = tk.Frame(frame1, bg="red", width=3, height=700) # LINEA FINITA
frame_parcel_add = tk.Frame(frame1, bg=main_color, width=350, height=150)
frame_parcel_button = tk.Frame(frame1, bg=main_color, width=400, height=550)

frame_prueba = tk.Frame(frame1, bg="blue", width=3, height=700)
frame_prueba.pack(side="right") # LINEA FINITA

frame2 = tk.Frame(root, width=500, height=700,bg=main_color) # INFO SCREEN

frame3 = tk.Frame(root, width=0, height=0, bg=main_color)
frame3.pack(side="right")

frame2.columnconfigure(0, weight=150)
frame2.columnconfigure(1, weight=200)
frame2.columnconfigure(2, weight=150)

# Alinear los frames en una fila vertical

frame_buttons.pack(side="left", anchor="e")
frame_parcel_add.pack(side="top", anchor="n")
frame_parcel_button.pack(side="top", anchor="n")

frame1.pack(side="left")
frame2.pack(side="left")
#frame3.pack(side="left")

# desactivar la posibilidad de cambiar el tamaño de la ventana
root.resizable(width=True, height=True)
root.configure(background=main_color)
root.geometry("1400x700")

def create_buttons():
    # Cambia el ancho del botón para que se ajuste a 3 botones por fila
    btn_width = 15

    resultados = mi_comunicacion.get_all()
    # total_rows = len(resultados)
    total_columns = 3

    for i, resultado in enumerate(resultados):
        # Calcular la fila / columna correspondiente
        row = i // total_columns
        col = i % total_columns

        # Crear el botón y agregarlo al marco
        new_button = MyButton(frame_parcel_button,
                                # ID = resultado = [0],
                                parcelNumber=resultado[1],
                                parcelDescription=resultado[2],
                                parcelSize=resultado[3],
                                parcelSpecies=resultado[4],
                                parcelStocking=resultado[5],
                                parcelLastGrazingDate=resultado[6],
                                restDays=resultado[7],
                                isActive=resultado[8],
                                grazinTime=resultado[9],
                                width=btn_width)

        new_button.grid(row=row, column=col, padx=2, pady=2)


def create_single_button():
    mi_comunicacion.crear_potrero_default()
    new_parcel = mi_comunicacion.get_last_potrero_number() # FUNCIONA -> obtiene ultimo potrero ingresado
    resultado = mi_comunicacion.get_all_parcel_info(new_parcel)

    # tomamos lo mismo de create_buttons
    btn_width = 15
    total_columns = 3

    # row = int(resultado[0][1])+1 // total_columns
    row = (int(new_parcel)-1) // total_columns
    # col = int(resultado[0][1]) % total_columns   
    col = (int(new_parcel)-1) % total_columns   

    new_button = MyButton(frame_parcel_button,
                        # ID = resultado = [0],
                        parcelNumber=resultado[0][1],
                        parcelDescription=resultado[0][2],
                        parcelSize=resultado[0][3],
                        parcelSpecies=resultado[0][4],
                        parcelStocking=resultado[0][5],
                        parcelLastGrazingDate=resultado[0][6],
                        restDays=resultado[0][7],
                        isActive=resultado[0][8],
                        grazinTime=resultado[0][9],
                        width=btn_width)

    new_button.grid(row=row, column=col, padx=2, pady=2)



    # crear boton trayendo los datos del recien creado y luego hacer la creacion como la funcion de crear todos los botones
    # create_buttons()

def delete_last_button():
    mi_comunicacion.delete_last_potrero()
    frame_parcel_button.winfo_children()[-1].destroy()

def add_parcel_button_click():
    create_single_button()

def delete_parcel_button_click():
    delete_last_button()

create_button = tk.Button(frame_parcel_add, text="Agregar potrero", command=add_parcel_button_click, background=boton_color)
create_button.pack(side=LEFT, pady=7, padx=8)

delete_button = tk.Button(frame_parcel_add, text="Eliminar último potrero", command=delete_parcel_button_click, background=boton_color)
delete_button.pack(side=LEFT, pady=7, padx=8)

create_buttons()


app = App(frame3)
app.pack()
app.config(background=main_color, bg=main_color)

# Mostrar la ventana
root.mainloop()