from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import inquirer
import Sauce
import Google
import SauceXpath

def mostrar_menu():
    preguntas = [
        inquirer.List('opcion',
                      message="Choose the way you want to execute the program",
                      choices=['By functions and JSON', 'By functions', 'By XPATH (complete flow)' ],
                      ),
    ]
    respuesta = inquirer.prompt(preguntas)
    if respuesta['opcion'] == 'By functions and Json':
        Sauce.load_users()
        Sauce.login_test()
    elif respuesta['opcion'] == 'By functions':
        Google.checkout()
    elif respuesta['opcion'] == 'By XPATH (complete flow)':
        SauceXpath.login_xpath()
        
mostrar_menu()