import sqlite3
from Connect import connect_bd

conexion= connect_bd("PythonHiberus")

def sacarcursos(nombrecategoria):
    try:
        cursor= conexion.cursor()
        sqlquerycat=('''
                  SELECT id FROM Categorias WHERE nombre = ?;
                  
                ''' )
        cursor.execute(sqlquerycat,(nombrecategoria,))
        categoria= cursor.fetchall()
        catid=categoria[0][0]
        sqlquerycur=('''
                  SELECT nombre FROM Cursos WHERE categoria_id = ?;
                  
                ''' )
        cursor.execute(sqlquerycur,(catid,))
        cursos=cursor.fetchall()
        
        
        for curso in cursos:
          print(curso[0])
        
    except sqlite3.Error as e:
        print(f"Error: {e}")
        
sacarcursos("Difícil")