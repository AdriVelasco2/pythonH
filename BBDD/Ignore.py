import sqlite3
from Connect import connect_bd
#if profesor== Matías o Juan
#   return IGNORA este archivo, es para pruebas


miConexion= connect_bd("BaseDePruebas")
cursor=miConexion.cursor()

sqlquery=('''
          CREATE TABLE IF NOT EXISTS PRODUCTOS
            (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOM_ARTICULO VARCHAR(50) UNIQUE,
              PRECIO INTEGER,
              SECCION VARCHAR(20) 
            );
            
            CREATE TABLE IF NOT EXISTS TIENDAS
            (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOM_TIENDA VARCHAR(50) UNIQUE,
              PROVINCIA VARCHAR(50),
              CIUDAD VARCHAR(50),
              SECCION_PROD VARCHAR(20) DEFAULT NULL,
              FOREIGN KEY(SECCION_PROD) REFERENCES PRODUCTOS(SECCION)
            );
          
          ''')

cursor.executescript(sqlquery)
miConexion.commit()

productos=[
    ("Muñeco",100,"Juguetes"),
    ("Patata",200,"Alimentación"),
    ("Coche",100,"Juguetes"),
    ("Cebollas",500,"Alimentación"),
]

tiendas=[
    ("Juguettos","ASTURIAS","Avilés",None),
    ("Frutas Pepe","GALICIA","Lugo",None),
    ("Majafrán","ASTURIAS","Oviedo",None),
    ("Panadería Paco","CANTABRIA","Vigo",None),
]

# INSERTAR EN BASE DE DATOS
cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)
cursor.executemany("INSERT INTO TIENDAS VALUES (NULL,?,?,?,?)",tiendas)

miConexion.commit()

# sqlqueryverProd=("SELECT * FROM PRODUCTOS")
# sqlqueryverTiendas=("SELECT * FROM TIENDAS")
# cursor.execute(sqlqueryverTiendas)
# vertiendas=cursor.fetchall()
# cursor.execute(sqlqueryverProd)
# # VER PRODUCTOS DE UNA BASE DE DATOS
# verproductos= cursor.fetchall()
# for producto in verproductos:
#     print("artículo: ",producto[1], " precio: ",producto[2], " pesetas")
# for tienda in vertiendas:
#     print(tienda)
# miConexion.commit()
# # SELECCIONAR PRODUCTOS DE UNA BASE DE DATOS
# sqlqueryleer= ("SELECT * FROM PRODUCTOS WHERE SECCION='Alimentación'")
# cursor.execute(sqlqueryleer)
# leerproductos=cursor.fetchall()
# for seccion in leerproductos:
#     print(seccion)
    
# miConexion.commit()
# # ACTUALIZAR UN PRODUCTO DE UNA BASE DE DATOS
# sqlqueryupdate=("UPDATE PRODUCTOS SET SECCION='Niñes' WHERE SECCION='Juguetes'")
# sqlqueryleerseccion= ("SELECT * FROM PRODUCTOS WHERE SECCION='Niñes'")

# cursor.execute(sqlqueryupdate)
# cursor.execute(sqlqueryleerseccion)
# actseccion=cursor.fetchall()
# for seccion in actseccion:
#     print(seccion)
# miConexion.commit()

# AHORA VOY A DARLE A LAS TIENDAS UNA SECCIÓN

miConexion.close()