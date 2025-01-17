import sqlite3
from Connect import connect_bd

conexion= connect_bd("PythonHiberus")

def insertcurso(nombrecurso,nombrecategoria):
    try:
        cursor= conexion.cursor()
        sqlquerycat=('''
                  SELECT id FROM categorias WHERE nombre = ?;
                  
                ''' )
        sqlquerycurso=('''
                  INSERT INTO Cursos(NOMBRE, CATEGORIA_ID) VALUES (?,?);
                ''' )
        cursor.execute(sqlquerycat,(nombrecategoria,))
        categoria= cursor.fetchall()
        catid= categoria[0][0]
        cursor.execute(sqlquerycurso,(nombrecurso,catid))
        
        conexion.commit()
        
        print(f"Se ha creado el curso: {nombrecurso} con la dificultad {nombrecategoria}")
       
        
    except sqlite3.Error as e:
        print(f"Error: {e}")
        
insertcurso("Javascript", "Patata")