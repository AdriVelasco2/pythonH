# Implementar un programa de Python para extraer y mostrar todas las etiquetas de encabezado de en.wikipedia.org/wiki/Main_Page.

import requests
from bs4 import BeautifulSoup
def server(url):
    try:
        response=requests.get(url, stream=True)
        content=response.content
        soup=BeautifulSoup(content, "html.parser")
        h1=soup.find_all('h1')
        
        if h1:
            for title in h1:
                print(title.text.strip())
        else:
            print("Esta web no se ha podido encontrar")
            
    except requests.exceptions.RequestException as e:
        print(f"No se ha podido acceder a la web, mensaje de error: {e}")
    
        
server("https://en.wikipedia.org/wiki/Main_Page")