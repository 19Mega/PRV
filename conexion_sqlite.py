
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
        
        
    
    def insertar_datos(self, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        bd = ''' INSERT INTO tabla_name (NOMBRE, EDAD, CORREO, TELEFONO) VALUES ('{}','{}','{}','{}',) '''.format(nombre, edad, correo, telefono)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def mostar_datos (self):
        cursor = self.conexion.cursor()
        bd= "SELECT * FROM datos"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
    
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM datos WHERE NOMBRE = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
    def actualiza_datos(self, ID, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        bd = '''UPDATE datos SET NOMBRE = '{}', EDAD = '{}', CORREO = '{}', TELEFONO = '{}' WHERE ID = '{}' '''.format(nombre, edad, correo, telefono, ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close() # cierra bd
        return dato
    
    def bd_save(self):
        cursor = self.conexion.cursor()
        bd = "INSERT INTO usuarios (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (parcelNumber, parcelDescription, parcelSize, parcelSpecies, parcelStocking, parcelLastGrazingDate, restDays, isActive, grazinTime)
                
        parcelNumber = None
        parcelDescription = None
        parcelSize = None
        parcelSpecies = None
        parcelStocking = None
        parcelLastGrazingDate = None
        restDays = None
        isActive = None
        grazinTime = None
    
    
    
    
    
    
    
    def get_parcelDescription(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelDescription FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelDescription(self, parcelNumber, parcelDescription):
        pass
        

    def get_parcelSize(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelSize FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelSize(self, parcelNumber, parcel_Size):
        pass
    
    def get_parcelSpecies(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelSpecies FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelSpecies(self, parcelNumber, parcelSpecies):
        pass
    
    def get_parcelStocking(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelStocking FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelStocking(self, parcelNumber, parcelStocking):
        pass
    
    def get_parcelLastGrazingDate(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT parcelLastGrazingDate FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_parcelLastGrazingDate(self, parcelNumber, parcelLastGrazingDate):
        pass
    
    def get_restDays(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT restDays FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_restDays(self, parcelNumber, restDays):
        pass
    
    def get_isActive(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT isActive FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_isActive(self, parcelNumber, isActive):
        pass
    
    
    def get_grazinTime(self, parcelNumber):
        cursor = self.conexion.cursor()
        bd = "SELECT grazinTime FROM campo WHERE parcelNumber = ?"
        cursor.execute(bd, (parcelNumber,))
        resultado = cursor.fetchall()[0][0]
        print("Resultado: ", resultado)
        return resultado
    
    def set_grazinTime(self, parcelNumber, grazinTime):
        pass
    
    
    
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






ventana = Comunication()
