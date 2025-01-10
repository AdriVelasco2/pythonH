
def pares():
    n=1000
    while n!=0:
        if n%2==0:
            yield n
            n-=2
        else:
            n-=1
        
gen =pares()
for _ in range(30):
    print(next(gen))
