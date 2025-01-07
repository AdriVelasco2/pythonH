# Menos mal que mi novia es profe de mates para ayudarme a entender como hallar el mcd
def mcd_euclidiano(a,b):
    
  if b==0:
    return a
  resto=a% b
# Llamamos a la función continuamente hasta que b sea cero y nos devuelva a.
  return mcd_euclidiano(b,resto)


print(mcd_euclidiano(24, 40)) #El resultado es 8.