import sqlite3
import os

#Conecto a la base de datos por separado.

def connect_bd(nombre):
    try:
        #Comprobamos si la base existe
        if not os.path.exists:
            print(f"Base de datos '{nombre}' creada.")
            
        # Si no existe la creamos, de existir solo se conectará
        miConexion=sqlite3.connect(nombre)
        print(f"Conectado a la base de datos: '{nombre}'")
        
        return miConexion
        

    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
