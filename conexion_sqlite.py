
# SELECT * FROM tabla;
# SELECT: Se utiliza para seleccionar datos de una tabla.

# INSERT INTO tabla (columna1, columna2) VALUES (valor1, valor2);
# INSERT: Se utiliza para insertar datos en una tabla.

# UPDATE tabla SET columna1 = valor1 WHERE columna2 = valor2;
# UPDATE: Se utiliza para actualizar datos en una tabla.

# DELETE FROM tabla WHERE columna1 = valor1;
# DELETE: Se utiliza para eliminar filas de una tabla.

# SELECT COUNT(*) FROM tabla WHERE columna1 = valor1;
# COUNT: Se utiliza para contar el número de filas que cumplen ciertas condiciones.

# conexion = sqlite3.connect('database.db') # Se utiliza para conectarse a una base de datos SQLite y devolver un objeto de conexión.
# cursor = conexion.cursor() # permite usar el .execute('Query')
# cursor.execute('SELECT * FROM tabla') # execute: Se utiliza para ejecutar comandos SQL en la base de datos.
# resultados = cursor.fetchall() # Se utiliza para obtener todos los resultados de una consulta.
# conexion.commit() # guarda bd
# conexion.close() # cierra bd


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
        
        # self.set_parcelDescription(4, "Descipcion actualizada") # FUNCIONA 
        # self.set_parcelSize(4, 5.2) # FUNCIONA
        # self.set_isActive(4, True) # FUNCIONA
        # self.set_parcelLastGrazingDate(4, datetime.now()) # FUNCIONA tiene que ser formato datetime
        # self.set_parcelSpecies(4, "Variadas con pasto miel") # FUNCIONA
        # self.set_parcelStocking(4, 25) # FUNCIONA
        # self.set_restDays(4, 12) # FUNCIONA
        # self.set_grazinTime(4, datetime.now()) # FUNCIONA        
        self.get_parcel_numbers_and_status()
    
    # GETTERS & SETTERS
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ------------------------------------------------------------------------
    
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


######################## # prueba 1

    def get_parcel_numbers_and_status(self):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelNumber, restDays, isActive FROM campo"
        cursor.execute(bd)
        resultados = cursor.fetchall()
        print("Resultado: ", resultados)
        return resultados
    
#########################

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






# ventana = Comunication()
