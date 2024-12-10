listToReverse=[1,2,3,4,5]

def reverseando(valor):
    print("La lista sin invertir es: ", valor)
    valor.sort(reverse=True)
    print("La lista invertida es: ",valor)
    
reverseando(listToReverse)