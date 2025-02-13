from behave import *
from utils import is_even

@given('I have the number {number}')
def step_give_number(context, number):
    context.number=int(number)
    
@when('I check if the number is even')
def step_when_number(context):
    context.result= is_even(context.number)

@then('the result should be {result}')
def step_then_number(context, result):
    expected_result= result.lower()=='true'
    print(f"Expected result: {expected_result}, Actual result: {context.result}")
    assert context.result==expected_result, f"Test failed for number {context.number}"