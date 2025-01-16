import sqlite3
from Connect import connect_bd

conexion= connect_bd("PythonHiberus")
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
            "Categorias",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL"
            )
    create_table(
        conexion,
        "Cursos",
        "id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL,FOREIGN KEY(categoria_id) REFERENCES categoria(id)"
    )
    print("Se han creado las tablas")
conexion.close()


