
def testVocal(caracter):
    vocales= 'aeiou'
    valor= False
    for letra in vocales:
        if (caracter == letra):
            valor= True
            return print ("Es vocal")    
    if not valor:
        print("No es vocal")
caracter = str(input("Introduce una letra: "))
testVocal(caracter)