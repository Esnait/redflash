from selenium import webdriver
import config


def init_driver():
    web_driver = None
    if config.BROWSER == 'chrome':
        web_driver = webdriver.Chrome(executable_path=config.DRIVER_PATH)
    if config.BROWSER == 'edge':
        web_driver = webdriver.Edge(executable_path=config.DRIVER_PATH)
    if config.BROWSER == 'firefox':
        web_driver = webdriver.Firefox(executable_path=config.DRIVER_PATH)

    web_driver.get(config.URL)
    web_driver.set_window_size(*config.SIZE.split("x"))
    return web_driver
