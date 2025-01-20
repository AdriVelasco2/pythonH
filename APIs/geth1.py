import requests
from bs4 import BeautifulSoup
def server(url):
    try:
        response=requests.get(url, stream=True)
        content=response.content
        soup=BeautifulSoup(content, "html.parser")
        h1=soup.find('h1')
        
        if h1:
            print(h1.text.strip())
        else:
            print("Esta web no se ha podido encontrar")
            
    except requests.exceptions.RequestException as e:
        print(f"No se ha podido acceder a la web, mensaje de error: {e}")
    
        
server("https://example.com")