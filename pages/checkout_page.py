from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
        self.checkout_button=(By.ID,"checkout")
        self.first_name=(By.ID,"first-name")
        self.last_name=(By.ID,"last-name")
        self.postal_code=(By.ID,"postal-code")
        self.continue_button=(By.ID,"continue")
        self.finish_button=(By.ID,"finish")

    def click_checkout(self):
       WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.checkout_button)).click()

    def enter_customer_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name)).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.finish_button)).click()