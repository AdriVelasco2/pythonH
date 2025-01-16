from Connect import connect_bd
import sqlite3

conexion= connect_bd("PythonHiberus")

def insert_category(nombre):
    try:
        cursor=conexion.cursor()
        sqlquery=f"INSERT INTO categorias (nombre) VALUES(?)"
        cursor.execute(sqlquery, (nombre,))
        conexion.commit()
        print(f"Categoría introducida: {nombre}")
    except sqlite3.Error as e:
        print(f"Error al introducir la categoría {e}")
    finally:
        cursor.close()

    
        
if conexion:
    category= input("Introduce nombre categoría: ")
    insert_category(category)
    print("Se ha creado el registro")
conexion.close