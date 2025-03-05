from behave import *
from utils import authenticate
@given('the user opens the login page')
def login_page(context):
    context.page = "Login Page Opened"
@when('they enter the username {username} and password {password}')
def login(context, username,password):
    context.result=authenticate(username,password)

@then('they should see the expected result {expected_result}')
def login_result(context, expected_result):
   assert expected_result==context.result,f"Expected {expected_result}, but got {context.result}"
    
# @given('the user is on the products page')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass
# @when('they search for a product named "<product_name>"')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass
# @then('they should see the search results')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass

# @given('the user is on the products page')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass
# @when('they add the product <product_name> to the cart')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass
# @then('the cart icon should display <expected_count>')
# def step_function(session: Session):
#     # Add Your Code Here
#     pass