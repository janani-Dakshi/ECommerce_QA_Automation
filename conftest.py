import pytest
import os
from selenium import webdriver

from pages.login_page import LoginPage
from test_data.login_data import USERNAME, PASSWORD
from config.config import BASE_URL

@pytest.fixture
def driver():
    options=webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
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
    driver.get(BASE_URL)

    login_page=LoginPage(driver)

    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    return driver

@pytest.fixture(autouse=True)
def screenshot_on_failure(request,driver):
    yield

    if request.node.rep_call.failed:
        os.makedirs("screenshots",exist_ok=True)
        driver.save_screenshot(f"screenshots/{request.node.name}.png")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome=yield
    rep=outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)
