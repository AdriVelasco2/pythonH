#Función Cervantes

def diccionarioRAE(Reverte):
    diccionario = {}
    for clave, valor in Reverte:
        #Si la clave no está añadida ya, se crea un nuevo elemento del diccionario
        if clave not in diccionario:
            diccionario[clave] = []
        diccionario[clave].append(valor)
    return diccionario


# Creo una lista random, a recordar que el primer valor actuará como clave.
lista = [('Barcelona', 'Castelldefells'), ('Madrid', 'Vallecas'), ('Barcelona', 'Gavá'), ('Barcelona', 'El Prat'), ('Asturias', 'Avilés')]

resultado = diccionarioRAE(lista)
print(resultado)