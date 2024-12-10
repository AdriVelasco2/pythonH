def bigger(num1, num2, num3):
    numbers=[num1,num2,num3]
    numbers.sort(reverse=True)
    print("El número mas grande es:", numbers[0])


bigger(5,4,3)

def biggerInput():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    numbers = [num1, num2, num3]
    numbers.sort(reverse=True)
    print("El número mas grande es:", numbers[0])

        
biggerInput()