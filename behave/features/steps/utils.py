def is_even(number):
    return number % 2==0
        
def basket_sum(number, add):
     total=number+add
     return total
 
VALID_USERS = {
    "standard_user": "secret_sauce",
    "admin_user": "admin_pass",
    "test_user": "test123"
}



def authenticate(username, password):
    return "success" if VALID_USERS.get(username) == password else "error"