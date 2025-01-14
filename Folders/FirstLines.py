import os

# Por más que he intentado, si no importo os y cambio el directorio, no me hace caso alguno
# En este código fuerzo al programa que coja el directorio indicado y lo use
os.chdir('C:/Users/AdrianVelascoCosta/Documents/PythonHiberus/pythonH/Folders/data')

def escribir(texto):   
    leer= open(texto, 'r')
    escribirFin= open(texto, 'a')
    for linea in leer:
        print (linea)
    with escribirFin as nuevaLinea:
        nuevaLinea.write("Hola pastelito")
try:
    escribir('leeme.txt')

finally:
    print("fin")