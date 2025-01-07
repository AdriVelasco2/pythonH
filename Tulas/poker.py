import random


palos=("Corazones", "Picas", "Diamantes", "Trébol")
cartas=("As","2", "3", "4", "5", "6", "7", "8","9","10","J","Q","K" )
baraja= []
mano=[]
comprobar=[]
contador=0
for valor in cartas:
    for palo in palos:
        baraja.append(f"{valor} de {palo}")

for i in range(4):
    aleatorio= random.choice(baraja)
    mano.append(aleatorio)
    
poker= [valor.split(" de ")[0]for valor in mano]

for i in range(len(poker)):
    comprobar.append(poker[i])
    if comprobar[i]==poker[i]:
        contador+1
        
if contador==4:
    print("Póker!!")
else:
    print("Te has arruinado :( ")
print(poker)

# De nuevo, no es la forma más eficiente de hacerlo, pero sí la que se me ha ocurrido sin recurrir a una IA