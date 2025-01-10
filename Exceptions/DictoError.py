
def exception(dict, clave):
    if clave not in dict:
        raise ValueError ("No se encuentra el apellido de este nombre")
    return dict[clave]


try:
    dict={'Pablo':'Menéndez', 'Matías':'Ceraño', 'Teresa':'Bartolomé'}
    print(exception(dict,'Teresa'))

    
except ValueError as error:
    print (error)
else:
    print("El valor se encuentra")