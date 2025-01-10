class Devolver():
    def __init__(self,cadena):
        self.cadena=cadena
    
    def devCadena(self):
        
        return self.cadena[-3:]
    
MostrarCadena= Devolver("Hola")
print(MostrarCadena.devCadena())
