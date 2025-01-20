import requests
import json
# IGNORAR ESTE ARCHIVO, ES UNA CAJA DE SASTRE

# if __name__ =='__main__':
#     url= 'https://www.google.es/'
#     response=  requests.get(url)
    
#     print(response)
    
#     if response.status_code==200:
#         # print(response.content)
#         content= response.content
#         file=open('google.html','wb')
#         file.write(content)
#         file.close()
        
# if __name__ =='__main__':
#     url= 'https://httpbin.org/get'
#     args={'nombre':'Adri', 'curso':'Python'}
#     response=  requests.get(url, params=args)
    
#     print(response.url)
#     # Obtener JSON
#     if response.status_code==200:
#         response_json=json.loads(response.text)
#         origin=response_json['origin']
#         print(origin)
        # print(response.content)
        # content= response.content
        # print(content)
        
    # POST
    
# if __name__ =='__main__':
#     url= 'https://httpbin.org/post'
#     payload={'nombre':'Adri', 'curso':'Python', 'nivel':'Fácil'}
#     headers={'Content-type':'application/json', 'access-token':'12345'}
#     response=  requests.post(url, data=json.dumps(payload), headers=headers)  
    
#     print(response.url)
#     # Obtener JSON
#     if response.status_code==200:
#         # print(response.content)
#        headers_response=response.headers
#        server=headers_response['server']
#        print(server)

# PUT & DELETE

# if __name__ =='__main__':
#     url= 'https://httpbin.org/delete'
#     payload={'nombre':'Adri', 'curso':'Python', 'nivel':'Fácil'}
#     headers={'Content-type':'application/json', 'access-token':'12345'}
#     response=  requests.delete(url, data=json.dumps(payload), headers=headers)  
    
#     print(response.url)
#     # Obtener JSON
#     if response.status_code==200:
#         # print(response.content)
#        headers_response=response.headers
#        server=headers_response['server']
#        print(server)
       
    #    Chunks
if __name__ =='__main__':
        url= 'https://th.bing.com/th/id/R.efdd7860e8137ee0f35a3c0410e56e6b?rik=95p35Ff7JVpLwA&riu=http%3a%2f%2f3.bp.blogspot.com%2f-8gnCYUNbyZ8%2fUgVGyoIybFI%2fAAAAAAAAAQc%2fXN1WcvlAaPI%2fs1600%2fmaine-coon-2.jpg&ehk=117E3qDZemBvasrY0AoXr990alLoriQFtavQWYcedC8%3d&risl=&pid=ImgRaw&r=0'
        # payload={'nombre':'Adri', 'curso':'Python', 'nivel':'Fácil'}
        # headers={'Content-type':'application/json', 'access-token':'12345'}
        response=  requests.get(url, stream=True)  #No descarga el contenido
        with open('header.txt','wb') as file:
            for chunk in response.iter_content(): #Descarga el contenido poco a poco
                file.write(chunk) 
        response.close()
        print(response.url)
#     # Obtener JSON
# if response.status_code==200:
#         # print(response.content)
#        headers_response=response.headers
#        server=headers_response['server']
#        print(server)
      