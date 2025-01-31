import sqlite3
from Connect import connect_bd

conexion= connect_bd("Selenium_Users")
def create_table(conexion,nombreTabla,params):
    try:
        miCursor= conexion.cursor()
        sqlquery= f"CREATE TABLE IF NOT EXISTS {nombreTabla} ({params})"
        miCursor.execute(sqlquery)
        conexion.commit()
        print(f"Tabla creadas {nombreTabla}")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla '{nombreTabla}': {e}")
    finally:
        miCursor.close()
        

if conexion:
    create_table(
            conexion,
            "Usuarios",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, password TEXT NOT NULL"
            )
    
    print("Se han creado las tablas")
conexion.close()


