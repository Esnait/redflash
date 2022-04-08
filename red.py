from lavander import *
from lavander import _find_element_
from selenium import webdriver
from selenium.webdriver.common.by import By

print("vanila")

page.driver = driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.set_window_size(1080, 900)







username = By.ID, "user-name"
password = By.ID, "password"
login = By.ID, "login-button"

logo = By.CSS_SELECTOR, ".app_logo"
header = By.CSS_SELECTOR, ".primary_header"


_find_element_(driver,username).send_keys("standard_user")
_find_element_(driver,password).send_keys("secret_sauce")
_find_element_(driver,login).click()

page(logo).is_centered(inside=header)

driver.quit()



#driver.find_element(loc)




