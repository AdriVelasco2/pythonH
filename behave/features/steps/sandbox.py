# from behave import *

# @given('A car is chosen')
# def step_given_a_car_is_chosen(context):
#     context.car = {"model": "Tesla Model S", "color": None}
#     print("Car model selected: Tesla Model S")

# @when('The user clicks on car color')
# def step_when_user_clicks_on_color(context):
#     context.available_colors = ["Red", "Blue", "White"]
#     print("User is choosing a color from:", context.available_colors)

# @then('The user choose a color {color}')
# def step_then_user_choose_color(context, color):
#     context.car["color"] = color
#     print(f"User chose the color: {color}")
#     # Validamos que el color está en la lista de colores disponibles
#     assert color in context.available_colors, f"Invalid color chosen: {color}"
#     assert context.car["color"] == color, "Color selection failed!"
