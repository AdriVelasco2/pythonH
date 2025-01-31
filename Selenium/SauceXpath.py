from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

driver= webdriver.Edge()

def login_xpath():
    driver.get("https://www.saucedemo.com/")
    user_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
    pass_input = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    user_input.send_keys("standard_user")
    pass_input.send_keys("secret_sauce",Keys.RETURN)
    shop_element=driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    shop_element.click()
    cart_button=driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
    cart_button.click()
    checkout=driver.find_element(By.XPATH,"//*[@id='checkout']")
    checkout.click()
    name=driver.find_element(By.XPATH, "//*[@id='first-name']")
    name.send_keys("Tyler")
    surname=driver.find_element(By.XPATH, "//*[@id='last-name']")
    surname.send_keys("Durden")
    driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("33400")
    driver.find_element(By.XPATH, "//*[@id='continue']").click()
    driver.find_element(By.XPATH, "//*[@id='finish']").click()
    driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()
    driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
    
    
    print("* "*20)
    input("✅💣Completely succesfull test. Press enter to finish test")
 
    
    
    
# def saludar():
#     print("La primera regla del club de la lucha, es que no se habla del club de la lucha")

# login_xpath()