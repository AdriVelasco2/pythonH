import requests

def server(url):
    try:
        response=requests.get(url)
        
        if response.status_code==200:
            print(f"la web {url} existe")
            
        else:
            print("Esta web no se ha podido encontrar")
            
    except requests.exceptions.RequestException as e:
        print(f"No se ha podido acceder a la web, mensaje de error: {e}")
    
        
server("https://www.google.es/")