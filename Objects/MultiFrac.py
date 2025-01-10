class Fraccion:
    def __init__(self,dividendo,divisor):
        if divisor==0:
                raise ValueError("No se puede dividir entre 0")
        self.dividendo=dividendo
        self.divisor=divisor
        
    def multiplicar(self,dividendo2,divisor2):
        return f"{self.dividendo*dividendo2}/{self.divisor*divisor2}"
    


resultado= Fraccion(5,6)
print(resultado.multiplicar(5,6))