import os

# Por más que he intentado, si no importo os y cambio el directorio, no me hace caso alguno
# En este código fuerzo al programa que coja el directorio indicado y lo use
os.chdir('C:/Users/AdrianVelascoCosta/Documents/PythonHiberus/pythonH/Folders/data')

def escribir(texto,textocifrado):
    cifrado=[]
    leer= open(texto, 'r+')
    for linea in leer:
        textoacifrar= chr(((ord(linea) - ord('a') + 13) % 26) + ord('a'))
        cifrado.append(textoacifrar)
    for linea in leer:
        print (linea)
    with open(textocifrado,'w') as nuevaLinea:
        for linea in cifrado:
            nuevaLinea.write(linea)
try:
    escribir('leeme.txt', 'Destinofinal.txt')

finally:
    print("fin")