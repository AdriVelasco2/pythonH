num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

numbers=[num1,num2,num3]

def suma(numbers):
    result= sum(numbers)
    print("La suma de los números es:", result)
    
suma(numbers)