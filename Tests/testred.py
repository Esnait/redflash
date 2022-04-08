from uilyt.properties import properties
from selenium.webdriver.common.by import By
from Tests.conftest import init_driver

driver = init_driver()

login_button = properties(driver, locator=(By.CSS_SELECTOR, ".button-login"))
header = properties(driver, locator=(By.CSS_SELECTOR, "#header .middle-wrapper"))
header_logo = properties(driver, locator=(By.CSS_SELECTOR, "#header-logo"))
doc_body = properties(driver, locator=(By.TAG_NAME, "body"))
head_label = properties(driver, locator=(By.CSS_SELECTOR, "div#header"))


def test_login_button():
    login_button.is_width("20").is_width("> 20").is_width("< 20").is_width("t34").is_width("2  to 5").is_squared()
    login_button.is_height("20").is_height("> 20").is_height("< 20").is_height("<>34").is_height(
        "2   to 5").is_almost_squared()
    header.is_centered_horizontally(inside=doc_body).is_centered_vertically(inside=doc_body) \
        .is_centered_vertically().is_centered_vertically(inside=header_logo).is_centered_horizontally(
        inside='red').is_centered_vertically(inside='red')
    header.is_inside(header_logo)
    login_button.is_left_of(header)

    print(header.get_font_family(), header.get_font_style(), header.get_rgba_font_color())
    header.is_font_size("14px").is_font_style('normal')
    header.is_size(header.get_size()['height'], header.get_size()['width'])
    header.is_centered_all(inside=head_label)
    print(header.get_attribute("class"))


def test_header():
    header_logo.is_centered_all()


test_login_button()
driver.quit()
