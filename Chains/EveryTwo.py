class Devolver():
    def __init__(self,cadena):
        self.cadena=cadena
    
    def devCadena(self):
        
        return self.cadena[::2]
    
MostrarCadena= Devolver("Hola Mundo")
print(MostrarCadena.devCadena())

