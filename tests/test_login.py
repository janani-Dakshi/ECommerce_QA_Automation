from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page=LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert login_page.get_page_title() == "Products"

    product_page=ProductPage(driver)
    product_page.add_backpack_to_cart()

    cart_page=CartPage(driver)
    cart_page.open_cart()

    assert cart_page.get_product_name() == "Sauce Labs Backpack"



