import tkinter as tk
from tkinter import *
from datetime import datetime
import sqlite3
from conexion_sqlite import Comunication
from tkinter import messagebox

mi_comunicacion = Comunication()
mi_comunicacion.rest_days_update()

# ID, parcelNumber, parcelDescription, parcelSize, parcelSpecies, 
# parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime

from tkinter import *

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
        self.config(text=f"N° {self.parcelNumber}  Descanso: {self.restDays} Días\n{'Activo' if self.isActive else 'Inactivo'}",
            font=("Arial", 9), fg="white", background="#5E6DA9", width=20, height=2, command=self.custom_callback)

    # COLOR BOTON: GRIS/inACTIVO
    def set_color_grey(self):
        self.config(text=f"N° {self.parcelNumber}  Descanso: {self.restDays} Días\n{'Activo' if self.isActive else 'Inactivo'}",
            font=("Arial", 9), fg="black", background="#9C9E9C", width=20, height=2, command=self.custom_callback)


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

            else:
                pass

    # PREGUNTA Terminar pastoreo
    def isActive_False(self):
        respuesta = messagebox.askquestion("Terminar pastoreo en potrero", "¿Desea terminar el pastoreo?")
        if respuesta == "yes":            
            # actualizamos isActive
            self.isActive = False
            mi_comunicacion.set_isActive(self.parcelNumber, self.isActive) 
            self.is_active_label.config(text='Sí' if self.isActive else 'No')

            # actualizar el rest days
            mi_comunicacion.rest_days_update()
            self.restDays = mi_comunicacion.get_restDays(self.parcelNumber)                
            self.restDays_label.config(text=self.restDays)

            # actualiza parcelLastGrazingDate 
            mi_comunicacion.set_parcelLastGrazingDate(self.parcelNumber, datetime.now()) 
            self.parcelLastGrazingDate = mi_comunicacion.get_parcelLastGrazingDate(self.parcelNumber)        
            self.parcelLastGrazingDate_label.config(text=self.parcelLastGrazingDate)

            # actualiza boton de potreros
            self.set_color_grey()

        else:
            pass


    # Elimina todos los widgets dentro del frame2.
    def clear_frame2(self):
        for widget in frame2.winfo_children():
            widget.destroy()



    # CREA LA SECCION DE INFO (cuando clicleamos un potrero)
    def custom_callback(self):

        self.clear_frame2()

        # parcelNumber
        Label(frame2, text="Potrero:",relief="solid", font=("Arial", 12), anchor="e").grid(row=0, column=0, sticky=W, pady=10,)
        Label(frame2, text=self.parcelNumber, relief="solid", font=("Arial", 12), anchor="w").grid(row=0, column=1, sticky=W, pady=2)

        # parcelDescription
        Label(frame2, text="Descripción de la Parcela:").grid(row=1, column=0, sticky=W, pady=2)
        Label(frame2, text=self.parcelDescription, relief="sunken").grid(row=1, column=1, sticky=W, pady=2)

        # parcelSize
        Label(frame2, text="Tamaño de la Parcela:").grid(row=2, column=0, sticky=W, pady=2)
        Label(frame2, text=f"{self.parcelSize} metros cuadrados", relief="sunken").grid(row=2, column=1, sticky=W, pady=2)

        # parcelSpecies
        Label(frame2, text="Especies en la Parcela:").grid(row=3, column=0, sticky=W, pady=2)
        Label(frame2, text=self.parcelSpecies, relief="sunken").grid(row=3, column=1, sticky=W, pady=2)

        # parcelStocking
        Label(frame2, text="Adecuación del Pastoreo:").grid(row=4, column=0, sticky=W, pady=2)
        Label(frame2, text=self.parcelStocking, relief="sunken").grid(row=4, column=1, sticky=W, pady=2)

        # parcelLastGrazingDate
        Label(frame2, text="Último Día de Pastoreo: ").grid(row=5, column=0, sticky=W, pady=2)
        self.parcelLastGrazingDate_label = Label(frame2, text="Hoy, en pastoreo" if self.isActive else self.parcelLastGrazingDate, relief="sunken")
        self.parcelLastGrazingDate_label.grid(row=5, column=1, sticky=W, pady=2)

        # restDays
        Label(frame2, text="Días de Descanso:").grid(row=6, column=0, sticky=W, pady=2)
        self.restDays_label = Label(frame2, text=self.restDays, relief="sunken")
        self.restDays_label.grid(row=6, column=1, sticky=W, pady=2)

        # isActive
        Label(frame2, text="Potrero Activo: ").grid(row=7, column=0, sticky=W, pady=2)
        self.is_active_label = Label(frame2, text='Sí' if self.isActive else 'No', relief="sunken")
        self.is_active_label.grid(row=7, column=1, sticky=W, pady=2)

        Button(frame2, text="Empezar pastoreo", command=self.isActive_True).grid(row=7, column=2, sticky=W, pady=2)
        Button(frame2, text="Terminar pastoreo", command=self.isActive_False).grid(row=8, column=2, sticky=W, pady=2)

        # Label(frame2, text="Tiempo de Pastoreo:").grid(row=8, column=0, sticky=W, pady=2)
        # Label(frame2, text=f"{self.diferencia} horas/día", relief="sunken").grid(row=8, column=1, sticky=W, pady=2)
        # Label(frame2, text=f"{self.diferencia} horas/día", relief="sunken", font=("Arial", 16), padx=10, pady=10).grid(row=8, column=1, sticky=W)

        Label(frame2, text="Tiempo de Pastoreo:").grid(row=8, column=0, sticky=W, pady=2)
        self.grazin_time_label = Label(frame2, text="{} días, {}:{:02d}".format(self.diferencia.days, self.diferencia.seconds // 3600, (self.diferencia.seconds // 60) % 60), relief="sunken")
        self.grazin_time_label.grid(row=8, column=1, sticky=W, pady=2)
        self.calcular_diferencia()

        # para poner " - " en restDays
        if self.isActive : self.restDays_label.config(text=" - ")







# Crear instancia de Tkinter
root = tk.Tk()

# Crear los tres frames (secciones verticales)
frame1 = tk.Frame(root, bg="#312f47", width=300, height=700)
frame_parcel_add = tk.Frame(frame1, bg="red", width=300, height=150)
frame_parcel_button = tk.Frame(frame1, bg="black", width=300, height=550)

frame2 = tk.Frame(root, bg="#3f3e52", width=400, height=700)
# Agregar un borde al frame de información
# frame2.config(relief="groove", borderwidth=2, padx=20, pady=10)


frame3 = tk.Frame(root, bg="blue", width=500, height=700)

# Alinear los frames en una fila vertical
frame1.pack(side="left")
frame2.pack(side="left")
frame3.pack(side="left")
frame_parcel_add.pack(side="top")
frame_parcel_button.pack(side="bottom")


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

    # Deshabilitar la posibilidad de cambiar de tamaño
    root.resizable(0, 0)

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



create_button = tk.Button(frame_parcel_add, text="+ Crear Potrero", command=create_single_button)
create_button.pack(pady=10, padx=10)

delete_button = tk.Button(frame_parcel_add, text="- Eliminar Potrero", command=delete_last_button)
delete_button.pack(pady=10, padx=10)

create_buttons()

# Mostrar la ventana
root.mainloop()