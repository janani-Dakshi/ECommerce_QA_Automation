from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from test_data.login_data import USERNAME, PASSWORD
from config.config import BASE_URL

def test_login(driver):
    driver.get(BASE_URL)

    login_page=LoginPage(driver)

    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    assert login_page.get_page_title() == "Products"

def test_invalid_login(driver):
    driver.get(BASE_URL)

    login_page=LoginPage(driver)
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    assert "Epic sadface" in driver.page_source