import requests
if __name__ =='__main__':
    url= 'https://www.google.es/'
    response=  requests.get(url)
    
    print(response)
    
    if response.status_code==200:
        print(response.content)