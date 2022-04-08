from lavander import *
from lavander import _find_element_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

print("vanila")

page.driver = driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.set_window_size(1080, 900)

# search_button = [(By.CSS_SELECTOR, ".primaryBtn.font24.latoBold.widgetSearchBtn"), (By.XPATH, "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")]
#
# twitter = By.CSS_SELECTOR, "span.twiiterIcon.landingSprite"
#
# print(_find_element_(driver, twitter).is_displayed())
# print(_find_element_(driver, search_button).is_displayed())
#
# print(page(search_button).WIDTH)
#
# page(search_button).is_width(216.5, approx=1).is_left(482, inside=twitter).is_top(402.0000).is_height(44).is_right_of(twitter)
#
# page(twitter).is_inside((By.TAG_NAME, "body")).is_left_of(search_button)
#
# page(twitter).check_top().equals(page(twitter).TOP)

#loc = id_, "button-login"
#loc2 = css_, "#header .middle-wrapper"

#print(Objects(driver, loc2))

#print(type(By.ID))
#print(type(css_))



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


#Object(driver, loc)

#driver.find_element(loc)


#driver.quit()


#print(loc.get_property('class'))
#header = Css, "yr"
