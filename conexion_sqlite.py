# conexion = sqlite3.connect('database.db') # Se utiliza para conectarse a una base de datos SQLite y devolver un objeto de conexión.
# cursor = conexion.cursor() # permite usar el .execute('Query')
# cursor.execute('SELECT * FROM tabla') # execute: Se utiliza para ejecutar comandos SQL en la base de datos.
# resultados = cursor.fetchall() # Se utiliza para obtener todos los resultados de una consulta.
# conexion.commit() # guarda bd
# conexion.close() # cierra bd

# def __init__(self, parcelNumber = None, parcelDescription = None, parcelSize = None, parcelSpecies = None,
#              parcelStocking = None, parcelLastGrazingDate = None, restDays = None, isActive = None, grazinTime = None):

from datetime import datetime
import sqlite3
from tkinter import *

class Comunication():
    def __init__(self):
        
        self.conexion = sqlite3.connect("prv.db") # FUNCIONA -> crea base datos
        self.crear_bd_table() # FUNCIONA -> crea tabla   
        
        # self.insertar_datos_prueba() # FUNCIONA -> prueba
        # self.get_last_potrero_number() # FUNCIONA -> obtiene ultimo potrero ingresado
        # self.crear_potrero_default() # FUNCIONA -> crea potrero
        # self.delete_last_potrero() # FUNCIONA -> elimina ultimo potrero ingresado
        # self.delete_potrero(6) # FUNCIONA -> eliminamos el num potrero que le pasemos
        
        # self.get_parcelDescription(4) # FUNCIONA 
        # self.get_parcelSize(4) # FUNCIONA
        # self.get_isActive(4) # FUNCIONA
        # self.get_parcelLastGrazingDate(4) # FUNCIONA
        # self.get_parcelSpecies(4) # FUNCIONA
        # self.get_parcelStocking(4) # FUNCIONA
        # self.get_restDays(4) # FUNCIONA
        # self.get_grazinTime(4) # FUNCIONA
        
        # self.set_parcelDescription(2, "Descipcion actualizada") # FUNCIONA 
        # self.set_parcelSize(2, 5.2) # FUNCIONA
        # self.set_isActive(1, True) # FUNCIONA
        # self.set_parcelLastGrazingDate(1, datetime.now()) # FUNCIONA tiene que ser formato datetime
        # self.set_parcelLastGrazingDate(3, datetime(2023, 2, 27, 11, 30, 15, 1234))
        # self.set_parcelSpecies(2, "Variadas con pasto miel") # FUNCIONA
        # self.set_parcelStocking(2, 25) # FUNCIONA
        # self.set_restDays(3, 12) # FUNCIONA
        # self.set_grazinTime(4, datetime.now()) # FUNCIONA        
        
        # self.set_parcelStockingForAll(60) # FUNCIONA 
        
        # self.get_parcel_numbers_and_status() # FUNCIONA  
        # self.get_all() # FUNCIONA  
        # self.get_all_parcel_info(1)
        
        # self.rest_days_update() # FUNCIONA 
        


#### 
    def rest_days_update(self):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelNumber, parcelLastGrazingDate FROM campo"
        cursor.execute(bd)
        resultado = cursor.fetchall()
        parcelNumber_restDays_list = []
        
        for parcelNumber, parcelLastGrazingDate in resultado:
            fecha = datetime.strptime(parcelLastGrazingDate, '%Y-%m-%d %H:%M:%S.%f')
            diferencia = datetime.now() - fecha
            parcelNumber_restDays_list.append((parcelNumber, diferencia.days))
        
        for parcelNumber, restDays in parcelNumber_restDays_list:
            #print("parcelNumber: ", parcelNumber)
            #print("restDays: ", restDays)
            bd_2 = "UPDATE campo SET restDays = ? WHERE parcelNumber = ?"
            cursor.execute(bd_2, (restDays, parcelNumber))
            self.conexion.commit()
            
    
    def set_parcelStockingForAll(self, parcelStocking):
        print(parcelStocking)
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelStocking = ?"
        cursor.execute(bd, (parcelStocking,))
        self.conexion.commit()


    # GENERAL FUNCTIONS
    
    def get_last_potrero_number(self): # FUNCIONA
        try:
            cursor = self.conexion.cursor()
            bd = "SELECT MAX(parcelNumber) FROM campo;"
            cursor.execute(bd) # hacemos la consulta
            resultado = cursor.fetchone()[0] # tomamos el ultimo parcelNumber de la tabla
            if resultado is None:
                print("No se encontraron potreros")
            return resultado
        except:
            pass

    def delete_last_potrero(self): # FUNCIONA
        try: 
            cursor = self.conexion.cursor()
            resultado = self.get_last_potrero_number()
            # print(resultado) # ELININAR
            bd_delete = "DELETE FROM campo WHERE parcelNumber = ?"
            cursor.execute(bd_delete, (resultado,))
            self.conexion.commit()
        except: 
            pass

    def delete_potrero(self, parcelNumber): # FUNCIONA
        print("en funcion delete_potrero: ", parcelNumber)
        parcelNumber = int(parcelNumber)
        cursor = self.conexion.cursor()
        bd_delete = "DELETE FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd_delete, (parcelNumber,))
        self.conexion.commit()
        
        

    def crear_potrero_default(self): # FUNCIONA
        cursor = self.conexion.cursor()
        
        try: parcelNumber = self.get_last_potrero_number() + 1
        except: parcelNumber = 1    
        
        parcelDescription = "Descripcion de potrero"
        parcelSize = 1
        parcelSpecies = "Variadas"
        parcelStocking = 0
        parcelLastGrazingDate = datetime.today()
        restDays = 0
        isActive = False
        grazinTime = datetime.now()
        
        bd = "INSERT INTO campo (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(bd, (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime))
        
        self.conexion.commit() # guarda bd


    # BD FUNCTIONS
    
    def crear_bd_table(self): # FUNCIONA
        cursor = self.conexion.cursor()
        
        bd = '''CREATE TABLE IF NOT EXISTS campo 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                parcelNumber INTEGER,
                parcelDescription TEXT,
                parcelSize FLOAT,
                parcelSpecies TEXT,
                parcelStocking INTEGER,
                parcelLastGrazingDate DATE,
                restDays INTEGER,
                isActive BOOLEAN,
                grazinTime DATETIME)'''
        
        cursor.execute(bd) # ejecuta query
        self.conexion.commit() # guarda bd
    

    def insertar_datos_prueba(self): # FUNCIONA
        cursor = self.conexion.cursor()
        
        parcelNumber = 1
        parcelDescription = "Descripcion de parcela"
        parcelSize = 1
        parcelSpecies = "Varias"
        parcelStocking = 20
        parcelLastGrazingDate = datetime.today()
        restDays = 10
        isActive = False
        grazinTime = datetime.now()
        
        bd = "INSERT INTO campo (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(bd, (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime))
        
        self.conexion.commit() # guarda bd
    
    
    # GETTERS & SETTERS
    
    ## Get all/some
    def get_parcel_numbers_and_status(self):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelNumber, restDays, isActive FROM campo"
        # bd = "SELECT * FROM campo"
        cursor.execute(bd)
        resultados = cursor.fetchall()
        print("Resultado: ", resultados)
        return resultados
    
    def get_all(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM campo"
        cursor.execute(bd)
        resultados = cursor.fetchall()
        print("Resultado: ", resultados)
        return resultados
    
    def get_all_parcel_info(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd,(parcelNumber,))
        resultados = cursor.fetchall()
        print("Resultado: ", resultados)
        return resultados
    
    # parcelDescription
    def get_parcelDescription(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelDescription FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelDescription(self, parcelNumber, parcelDescription):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelDescription = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelDescription, parcelNumber))
        self.conexion.commit()
    
    # parcelSize
    def get_parcelSize(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelSize FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelSize(self, parcelNumber, parcelSize):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelSize = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelSize, parcelNumber))
        self.conexion.commit()
    
    # parcelSpecies
    def get_parcelSpecies(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelSpecies FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelSpecies(self, parcelNumber, parcelSpecies):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelSpecies = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelSpecies, parcelNumber))
        self.conexion.commit()
    
    # parcelStocking
    def get_parcelStocking(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelStocking FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelStocking(self, parcelNumber, parcelStocking):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelStocking = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelStocking, parcelNumber))
        self.conexion.commit()
    
    # parcelLastGrazingDate
    def get_parcelLastGrazingDate(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelLastGrazingDate FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelLastGrazingDate(self, parcelNumber, parcelLastGrazingDate):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET parcelLastGrazingDate = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelLastGrazingDate, parcelNumber))
        self.conexion.commit()
    
    # restDays
    def get_restDays(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT restDays FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_restDays(self, parcelNumber, restDays):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET restDays = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (restDays, parcelNumber))
        self.conexion.commit()
    
    # isActive
    def get_isActive(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT isActive FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_isActive(self, parcelNumber, isActive):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET isActive = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (isActive, parcelNumber))
        self.conexion.commit()
    
    # grazinTime
    def get_grazinTime(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT grazinTime FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_grazinTime(self, parcelNumber, grazinTime):
        cursor = self.conexion.cursor()
        bd = "UPDATE campo SET grazinTime = ? WHERE parcelNumber = ?"
        cursor.execute(bd, (grazinTime, parcelNumber))
        self.conexion.commit()
    
ventana = Comunication()