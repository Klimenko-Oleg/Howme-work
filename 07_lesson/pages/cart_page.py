from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.checkout_button = (
            By.CSS_SELECTOR,
            "[data-test='checkout']"
        )  # Используем data-test

    def click_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
