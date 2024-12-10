palos=["Corazones", "Picas", "Diamantes", "Trébol"]
cartas=["As","2", "3", "4", "5", "6", "7", "8","9","10","J","Q","K" ]

# for valor, palo in zip(cartas, palos):
#     print(valor, palo)
# Dejo esto como constancia de que he probado otras cosas pero no he encontrado una mejor manera
    

for valor in cartas:
    for palo in palos:
        print (valor, palo)
        

# Sé que no es ideal la representación de la baraja pero es válida, ¿no? jeje