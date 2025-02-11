import requests
import os
import json

os.chdir('C:/Users/AdrianVelascoCosta/Documents/PythonHiberus/pythonH/')

def upload_pet_image(pet_id, image_path):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage"
    
    
    try:
        # rb no significa Red Bull, es para que lo lea como binario y no intente convertir en testo una imagen
        with open(image_path, "rb") as image_file:
            files = {
                "file": 'imgtest.png'
            }
            response = requests.post(url, files=files)
            response.raise_for_status()
            print("Image upload.")
            print("Server response", response.json())
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except FileNotFoundError:
        print(f"Image doesnt found in path:  '{image_path}'.")
    except requests.exceptions.RequestException as req_err:
        print(f"request error: {req_err}")
    except Exception as err:
        print(f"Error Unexpected: {err}")

# upload_pet_image(12, "imgtest.png")

def create_pet(pet_id, name, status):
    url = "https://petstore.swagger.io/v2/pet"
    headers = {
        "Content-Type": "application/json"
    }
    pet_data = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(pet_data))
        response.raise_for_status()
        
        created_pet = response.json()
        print("Successfull creation of pet: ")
        print(f"ID: {created_pet['id']}")
        print(f"Name: {created_pet['name']}")
        print(f"Status: {created_pet['status']}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error Unexpected: {err}")

# create_pet(33, "Alonso", "available")

def update_pet_form_data(pet_id, name, status):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
   
    data = {
        "name": name,
        "status": status
    }
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        
        updated_pet = response.json()
        print("Successfull creation of pet: ")
        print(updated_pet)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error Unexpected: {err}")

# update_pet_form_data(2,"Alonso", "Available")

def create_order(order_id, pet_id, quantity, status, complete=True):
    url = "https://petstore.swagger.io/v2/store/order"


    order_data = {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": "2025-02-04T12:00:00Z",   
        "status": status,   
        "complete": complete
    }
    
    try:
        response = requests.post(url, data=json.dumps(order_data))
        response.raise_for_status()
        
        order = response.json()
        print("Order created successfully")
        print(f"Order ID: {order['id']}")
        print(f"Pet ID: {order['petId']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Satus: {order['status']}")
        print(f"Ship date: {order['shipDate']}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error Unexpected: {err}")

# create_order(1001,12345,2,"placed")

def create_users(users_list):
    url = "https://petstore.swagger.io/v2/user/createWithArray"
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(users_list))
        response.raise_for_status()
        
        print("Usuarios creados con éxito.")
        print(f"Código de respuesta: {response.status_code}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error inesperado: {err}")


users = [
    {
        "id": 1,
        "username": "El nano",
        "firstName": "Fernando",
        "lastName": "Alonso",
        "email": "Aston@martin.com",
        "password": "stroll",
        "phone": "123456789",
        "userStatus": 1
    }
    
]


# create_users(users)

def create_users_array(users_array):
    url = "https://petstore.swagger.io/v2/user/createWithList"
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(users_array))
        response.raise_for_status()
        
        print("Usuarios creados con éxito.")
        print(f"Código de respuesta: {response.status_code}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error inesperado: {err}")





# create_users_array(user)

def create_user(user):
    url = "https://petstore.swagger.io/v2/user"
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(user))
        response.raise_for_status()
        
        print("Usuarios creados con éxito.")
        print(f"Código de respuesta: {response.status_code}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error inesperado: {err}")


user= {
        "id": 1,
        "username": "El nano",
        "firstName": "Fernando",
        "lastName": "Alonso",
        "email": "Aston@martin.com",
        "password": "stroll",
        "phone": "123456789",
        "userStatus": 1
    }
    



create_user(user)