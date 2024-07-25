import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://store.epicgames.com/ru/')
    driver.maximize_window()
    yield driver
    driver.quit()