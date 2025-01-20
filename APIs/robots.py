import requests

def server(url):
    try:
        response=requests.get(f'{url}/robots.txt')
        
        if response.status_code==200:
            print(f"el contenido de {url}/robots.txt es: ", response.text)
            
        else:
            print("Esta web no se ha podido encontrar")
            
    except requests.exceptions.RequestException as e:
        print(f"No se ha podido acceder a la web, mensaje de error: {e}")
    
        
server("https://en.wikipedia.org")