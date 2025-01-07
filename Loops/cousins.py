#Un número primo es aquel que solo es divisible entre sí mismo y la unidad. Yo suspendía Mates que conste, fui por letras.
def cousins(number):
    i = 2
    result = []
    # Este bucle continúa mientras el cuadrado del divisor actual sea menor o igual al número, ya que no tendría sentido que fuese mayor
    while i * i <= number:
        # Si al dividir el resultado no es cero exacto, sumamos uno al divisor
        if number % i:
            i += 1
        # Si es cero exacto, se suma el divisor a la descomposición.
        else:
            number //= i
            result.append(i)
        #Si queda algún número, significa que es primo y lo añadimos a la descomposición.
    if number > 1:
        result.append(number)
    return result


print(cousins(20))


# Nota: La explicación es para acordarme en el futuro de cómo se hace.