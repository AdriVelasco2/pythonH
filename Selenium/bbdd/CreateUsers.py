from Connect import connect_bd
import sqlite3

conexion= connect_bd("Selenium_users")

def insert_user(nombre, password):
    try:
        cursor=conexion.cursor()
        sqlquery=f"INSERT INTO Usuarios (nombre,password) VALUES(?,?)"
        cursor.execute(sqlquery, (nombre, password))
        conexion.commit()
        print(f"Usuario introducido: {nombre}")
    except sqlite3.Error as e:
        print(f"Error al introducir el usuario {e}")
    finally:
        cursor.close()

    
        
if conexion:
    USER= input("Introduce un usuario: ")
    PASSWORD= input("Introduce la contraseña: ")
    
    insert_user(USER,PASSWORD)
    print("Se ha creado el registro")
conexion.close
