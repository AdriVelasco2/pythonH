class Devolver():
    def __init__(self,cadena1, cadena2):
        self.cadena1=cadena1
        self.cadena2=cadena2
    
    def devCadena(self):
        return self.cadena2 in self.cadena1
    
MostrarCadena= Devolver("Hola Mundo", "Mundo")
print(MostrarCadena.devCadena())
