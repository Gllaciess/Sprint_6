import pytest
from selenium import webdriver
from pages.main_page import MainPage
from constants import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    driver.get(Urls.BASE_URL)
    main_page.accept_cookies()
    return main_page


    