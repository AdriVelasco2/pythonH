class Devolver():
    def __init__(self,cadena):
        self.cadena=cadena
    
    def devCadena(self):
        if len(self.cadena) <2:
            return self.cadena
        return self.cadena[:2]
    
MostrarCadena= Devolver("Hola")
print(MostrarCadena.devCadena())
