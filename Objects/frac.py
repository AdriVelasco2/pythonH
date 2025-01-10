class Fraccion:

    def __init__(self,dividendo,divisor):
        if divisor==0:
                raise ValueError("No se puede dividir entre 0")
        self.dividendo=dividendo
        self.divisor=divisor
        
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"
      
mostrarFraccion= Fraccion(5,6)
print(mostrarFraccion)