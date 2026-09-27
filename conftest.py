import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options=webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-features=PasswordLeakDetection")
    
    options.add_experimental_option (
        "prefs",
        {
            "Credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    
    )

    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")

    login_page=LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    return driver