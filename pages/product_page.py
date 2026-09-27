from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
        self.backpack=(By.ID,"add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack).click()
