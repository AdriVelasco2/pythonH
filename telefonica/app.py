import requests

BASE_URL = "https://petstore.swagger.io/v2"

def get_pet(pet_id):
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    if response.status_code == 200:
        print("Mascota encontrada:", response.json())
    else:
        print("Error:", response.status_code, response.text)

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

if __name__ == "__main__":
    add_pet() 
    get_pet(1001)
