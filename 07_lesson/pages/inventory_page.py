from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_button).click()

    def add_tshirt_to_cart(self):
        self.driver.find_element(*self.tshirt_add_button).click()

    def add_onesie_to_cart(self):
        self.driver.find_element(*self.onesie_add_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
