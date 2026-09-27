from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from test_data.login_data import USERNAME, PASSWORD

def test_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page=LoginPage(driver)

    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    assert login_page.get_page_title() == "Products"