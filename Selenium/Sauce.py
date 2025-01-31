from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import os
import json

os.chdir('C:/Users/AdrianVelascoCosta/Documents/PythonHiberus/pythonH/Selenium/data')


def load_users():
    with open("Seed.json","r") as file:
        return json.load(file)


def login_test(): 
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    FILE_USERS= load_users()
    driver.get("https://www.saucedemo.com/")
    
    for user_name in FILE_USERS:
        print(f"{user_name}")
        username= user_name["username"]
        password= user_name["pass"]
        username_input = driver.find_element(By.NAME, "user-name")
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        username_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password,Keys.RETURN)
        if "inventory.html" in driver.current_url:
            driver.back()
    input("Succesfull test, press enter to finish the test")


    # Verificar si la contraseña ingresada coincide con la de la base de datos
    # if PASSWORD:
    #     print("Inicio de sesión exitoso.")

    #     # Interactuar con la web
    #     user = driver.find_element(By.NAME, "user-name")
    #     password = driver.find_element(By.NAME, "password")

    #     user.send_keys(USERNAME)
    #     password.send_keys(PASSWORD, Keys.RETURN)

    # else:
    #     print("Contraseña incorrecta.")
    #     driver.quit()
    #     exit()

    # all_links = driver.find_elements(By.TAG_NAME, "a")
    # for link in all_links:
    #     print (link.text)
    # cart=driver.find_elements(By.NAME,"add-to-cart-sauce-labs-backpack")
    # cart[0].click()
# shop=driver.find_elements(By.ID,"shopping-cart-link")

# login_test()
