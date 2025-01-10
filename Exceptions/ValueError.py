
def exception(lista, elemento):
    if elemento in lista:
        raise ValueError ("El nombre ya se añadió a la lista")
    lista.append(elemento)
    return lista


try:
    nombres=[]
    print(exception(nombres,"marco"))
    print(exception(nombres,"Polo"))
    print(exception(nombres,"marco"))
    
    
except ValueError as error:
    print (error)
else:
    print("Se ha añadido el valor")