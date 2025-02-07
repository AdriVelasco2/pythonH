import requests

# if __name__ =='__main__':
#     url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
#     args={"pet_id":"1"}
#     response=  requests.get(url, params=args)
    
#     print(response.url)
#     # Obtener JSON
#     if response.status_code==200:
#         response_json=json.loads(response.text)
#         origin=response_json['origin']
#         print(origin)
#         print(response.content)
#         content= response.content
#         print(content)
        
def get_pet_byid(pet_id):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    
    try:
        response = requests.get(url)
         
        pet=response.json()
        
        print("Pet information:")
        for key,value in pet.items():
            print(value)
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Pet not found, status code: 404")
            
# get_pet_byid(1)

def get_pets_bystatus(status):
    url = f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}"
    try:
        response = requests.get(url)
         
        pet=response.json()
        if not pet:
            print(f"Pet not found with status:  '{status}'.")
            return
        print("Pet status:")
        print(pet)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Status not found, response code: 404")
            
# get_pets_bystatus('available')

def get_pets_inventory():
    url = f"https://petstore.swagger.io/v2/store/inventory"
    try:
        response = requests.get(url)
         
        inventory=response.json()
        
        print("inventory info:")
        print(inventory)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Status not found, response code: 404")
            
# get_pets_inventory()

def get_pet_orders(order_id):
    url = f"https://petstore.swagger.io/v2/store/order/{order_id}"
    try:
        response = requests.get(url)
         
        order=response.json()
        if not order:
            print(f"Order not founds with the id:  '{order_id}'.")
            return
        print("Pet status:")
        print(order)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Status not found, response code: 404")

# get_pet_orders(1)


def get_pet_user(user):
    url = f"https://petstore.swagger.io/v2/user/{user}"
    try:
        response = requests.get(url)
        
        user=response.json()
        if not user:
            print(f"user not founds with the username:  '{user}'.")
            return
        print("User:")
        print(user)
        print(response.status_code)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code==404:
            print("Status not found, response code: 404")
            


def test_get_pet_user_status_code():
    user = "string" 
    response = get_pet_user(user)
    assert response.status_code == 200



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
            
get_login('string','string')