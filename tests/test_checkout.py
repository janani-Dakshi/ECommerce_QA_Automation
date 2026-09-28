from selenium.webdriver.common.by import By

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.waits import wait_for_element
from test_data.checkout_data import FIRST_NAME, LAST_NAME, POSTAL_CODE

def test_checkout_flow(logged_in_driver):
    driver=logged_in_driver

    product_page=ProductPage(driver)
    product_page.add_backpack_to_cart()

    cart_page=CartPage(driver)
    cart_page.open_cart()

    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    checkout_page=CheckoutPage(driver)
    checkout_page.click_checkout()

    checkout_page.enter_customer_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.click_continue()
    checkout_page.click_finish()

    confirmation = wait_for_element(driver,(By.CLASS_NAME,"complete-header"))
    assert confirmation.text=="Thank you for your order!"
    

