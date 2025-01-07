def wordcounting(text):
    # Cogemos las palabras del texto, las separamos una a una y lo pasamos a minúscula, si quito el .lower funcionaría, solo que la misma palabra se podría repetir dos veces y es una movida
    words = text.lower().split()

    diccionario = {}
    
    for word in words:
        # Cogemos palabra a palabra lo que hemos guardado en words y si aparece, le sumamos uno al contador, en este caso, digamos que se guardará como clave y valor, parecido al otro ejercicio de diccionarios
        diccionario[word] = diccionario.get(word, 0) + 1
    return diccionario


text = "Canta conmigo: A veces gritas desde el cielo, queriendo destrozar mi calma, vas persiguiendo como un trueno para darme ese relámpago azul. Ahora me gritas desde el cielo, pero te encuentras con mi alma. Conmigo ya no intentes nada, parece que el amor me calma"
result = wordcounting(text)
print(result)

#Nota: no está ignorando las comas. Como no quiero usar ChatGpt y lo he hecho por mi cuenta, GPT sí que me lo da quitando comas y otros signos de puntuación.