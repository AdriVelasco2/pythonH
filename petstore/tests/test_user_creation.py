import pytest
import random
from create_user import create_user
from get_pet_by_id import get_pet_by_id
 
user_data = {
    "id": 10,
    "username": "newuser123",
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe123@example.com",
    "password": "password123",
    "phone": "123-456-7890",
    "userStatus": 1  
}

def test_create_user():
    response = create_user(user_data)
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
def test_get_pet_by_id():
    response =get_pet_by_id(random.randint(1, 20))
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
