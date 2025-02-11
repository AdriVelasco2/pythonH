import requests
import json


def get_pet_by_id(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
   
    
    response = requests.get(url)
    
    return response
