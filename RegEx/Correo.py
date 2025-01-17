import re

def regexcorreo(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(regex, email):
        return True
    else:
        return False

correo = input("Introduce una dirección de correo válida")
if regexcorreo(correo):
    print(f"El correo '{correo}' es válido.")
else:
    print(f"El correo '{correo}' no es válido.")
