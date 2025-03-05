import requests

BASE_URL = "https://petstore.swagger.io/v2"

def get_pet(pet_id):
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    if response.status_code == 200:
        pet_data=response.json()
        
        print("Mascota encontrada:", response.json())
    else:
        print("Error:", response.status_code, response.text)

def get_pets_bystatus(status):
    url = f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}"
    try:
        response = requests.get(url)
        pets_dict = {} 

        for pet in response:
            pets_dict[pet['id']] = pet['name']
            
        print(pets_dict)
         
        pet=response.json()
        if not pet:
            print(f"Pet not found with status:  '{status}'.")
            return
        print("Pet status:")
        print(pet)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Status not found, response code: 404")
            

def add_pet():
    pet_data = {
        "id": 1001,
        "category": {"id": 1, "name": "dog"},
        "name": "Firulais",
        "photoUrls": ["https://example.com/firulais.jpg"],
        "tags": [{"id": 1, "name": "cachorro"}],
        "status": "available"
    }
    
    response = requests.post(f"{BASE_URL}/pet", json=pet_data, headers={"Content-Type": "application/json"})
    if response.status_code == 200 or response.status_code == 201:
        print("Mascota añadida:", response.json())
    else:
        print("Error al añadir mascota:", response.status_code, response.text)
        
def get_login(username,password):
    url = f"https://petstore.swagger.io/v2/user/login?username={username}&password={password}"
    try:
        response = requests.get(url)
         
        user=response.json()
        if not user:
            print(f"user not founds with the username:  '{username}'.")
            return
        print("Login correcto")
        print(user)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("User not found, response code: 404")

if __name__ == "__main__":
    add_pet() 
    get_pet(1001)
    get_pets_bystatus('available')
    get_login('string','string')
