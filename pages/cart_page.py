from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self,driver):
        self.driver=driver

        self.cart=(By.CLASS_NAME,"shopping_cart_link")
        self.backpack=(By.CLASS_NAME,"inventory_item_name")

    def open_cart(self):
        self.driver.find_element(*self.cart).click()

    def get_product_name(self):
        return self.driver.find_element(*self.backpack).text