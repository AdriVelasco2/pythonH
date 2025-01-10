# En este último ejercicio, a diferencia de los otros, la cadena está inicializada en la propia clase
# De esta manera podemos hacerla recursiva las veces que queramos.
# En el resto de ejercicios de cadenas, solo podías construir una por objeto

class Devolver():
    cadena1=""
    cadena2=""
    def __init__(self):
        pass
    
    def devCadena(self,param1,param2):
        self.cadena1=param1
        self.cadena2=param2
        if self.cadena1 < self.cadena2:
            return self.cadena1
        return self.cadena2
    
MostrarCadena= Devolver()
print(MostrarCadena.devCadena("a","b"))
print(MostrarCadena.devCadena("b","a"))

