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
   
   
   
@given("the user is on the products page")
def step_open_products_page(context):
    context.page = "Products Page Opened"

@when("they search for a product named {product_name}")
def step_search_product(context, product_name):
    context.product = product_name  # Behave pasa los valores automáticamente desde Examples

@then("they should see the search results")
def step_verify_search_results(context):
    available_products = [context.product]
    
    product_found = any(context.product.lower() in p.lower() for p in available_products)
    assert product_found, f"Product '{context.product}' not found!"
    

@given('the user is already on the products page')
def step_products(context):
    context.page = "Products Page Opened"
    
@when('they add the product {product_name} to the cart')
def step_add(context, product_name):
    context.product=product_name
 
@then('the cart icon should display {expected_count}')
def step_cart_icon(context, expected_count):
    context.count=int(expected_count)
    
    assert int(context.count)==int(expected_count), f"Expected length: {context.count}, but got {expected_count}"
    
    
@given('the user has products in the cart')
def step_cart_products(context):
    context.cart = ["Sauce Labs Backpack", "Bike Light"]
@when('they complete the checkout process with {first_name}, {last_name}, and {zip_code}')
def step_checkout(context, first_name, last_name, zip_code):
    context.name=first_name
    context.surname=last_name
    context.code=zip_code
    context.order_confirmation = "Thank you for your order!"
@then('they should see the confirmation message "Thank you for your order!"')
def step_confirm(context):
    assert context.order_confirmation == "Thank you for your order!", f"Expected 'Thank you for your order!', but got '{context.order_confirmation}'"