import sqlite3
from Connect import connect_bd

conexion= connect_bd("PythonHiberus")

def sacarcursos(nombrecategoria):
    try:
        cursor= conexion.cursor()
        sqlquerycur=('''
                  SELECT nombre FROM Cursos WHERE nombre = ?;
                  
                ''' )
        cursor.execute(sqlquerycur,(nombrecategoria,))
        categoria= cursor.fetchall()
        catid=categoria[0][0]
        sqlquerycat=('''
                  SELECT nombre FROM Cursos WHERE categoria_id = ?;
                  
                ''' )
        cursor.execute(sqlquerycat,(nombrecategoria,catid))
        cursos=cursor.fetchall()
        conexion.commit()
        for curso in cursos:
            print (curso[0])
       
        
    except sqlite3.Error as e:
        print(f"Error: {e}")
        
sacarcursos("Difícil")