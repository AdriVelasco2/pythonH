class Coche():
    color='azul'
    precio=1000
    puertas=5
    vendido=False
    
    def venta (self, vendemos):
        self.vendido=vendemos
        if (self.vendido):
            return "El coche está vendido"
        else:
            return "Hay Stock del coche"
    
    def estado(self):
        print("El coches es de color:", self.color, "y tiene: ", self.puertas)
        
ventaCoche=Coche()

print("Este coche se vende por:", ventaCoche.precio)

print(ventaCoche.venta(True))
ventaCoche.estado()

print("Vamos a diferenciar--------------------")

ventaCoche2=Coche()
print(ventaCoche2.venta(False))
