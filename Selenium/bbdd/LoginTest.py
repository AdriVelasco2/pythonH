from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from Connect import connect_bd

conexion= connect_bd("Selenium_users")
miCursor= conexion.cursor()
driver = webdriver.Edge()
def login_test(USERNAME, PASSWORD): 
    driver.get("https://www.saucedemo.com/")
    USER_NAME= USERNAME
    PASS_WORD= PASSWORD
    SQL_USER = "SELECT password FROM Usuarios WHERE nombre = ?"
    miCursor.execute(SQL_USER, (USERNAME,))
    resultado = miCursor.fetchone()
    user = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")
    stored_password = resultado[0]

    # Verificar si la contraseña ingresada coincide con la de la base de datos
    if PASSWORD == stored_password:
        print("Inicio de sesión exitoso.")

        # Interactuar con la web
        user = driver.find_element(By.NAME, "user-name")
        password = driver.find_element(By.NAME, "password")

        user.send_keys(USERNAME)
        password.send_keys(PASSWORD, Keys.RETURN)

    else:
        print("Contraseña incorrecta.")
        driver.quit()
        exit()

    all_links = driver.find_elements(By.TAG_NAME, "a")
    for link in all_links:
        print (link.text)
    cart=driver.find_elements(By.NAME,"add-to-cart-sauce-labs-backpack")
    cart[0].click()
# shop=driver.find_elements(By.ID,"shopping-cart-link")

login_test(input("Introduce nombre de usuario: "), input("Introduce contraseña: "))
input("Press enter to finish the test")