import requests
import json

def create_user(user_data):
    url = "https://petstore.swagger.io/v2/user"
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(user_data))
    
    return response
