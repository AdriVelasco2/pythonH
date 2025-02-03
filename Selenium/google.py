from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

def checkout():

    driver = webdriver.Edge()

    driver.get("https://www.saucedemo.com/")
    # aceptar_cookies = driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar todo']")
    # aceptar_cookies.click()
    # print("Cookies aceptadas")
    user = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")

    user.send_keys("standard_user", )
    password.send_keys("secret_sauce", Keys.RETURN)
    all_links = driver.find_elements(By.TAG_NAME, "a")
    for link in all_links:
        print (link.text)
    cart=driver.find_elements(By.NAME,"add-to-cart-sauce-labs-backpack")
    cart[0].click()
    shop=driver.find_elements(By.ID,"shopping-cart-link")
   

    input("Press enter to finish the test")

# results= elem.find_elements(By.CSS_SELECTOR, "h2")
# for result in results:
#     print(result.text)
# result_link= elem.find_elements(By.ID, "b-scopeListItem-news")
# # result_link[0].click()
# galletitas= driver.get_cookies()
# print("Cookies: ")
# for cookie in galletitas:
#     print(cookie)