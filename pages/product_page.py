from selenium.webdriver.common.by import By
from utils.waits import wait_for_element, EC

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
        self.backpack=(By.ID,"add-to-cart-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        wait_for_element(self.driver,self.backpack).click()
