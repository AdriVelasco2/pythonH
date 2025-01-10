def multiplos(n):
    divisor=3
    print("Estos son los múltiplos de 3 de ese número:")
    while n%divisor==0:
            yield n
            n-=3
            if n<=0:
                break
    
            
gen= multiplos(9)
for _ in range(3):
    print(next(gen))
