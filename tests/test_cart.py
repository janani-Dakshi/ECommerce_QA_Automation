import pytest

from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_add_product_to_cart(logged_in_driver):
    driver=logged_in_driver

    product_page=ProductPage(driver)
    product_page.add_backpack_to_cart()

    cart_page=CartPage(driver)
    cart_page.open_cart()

    assert cart_page.get_product_name() == "Sauce Labs Backpack"