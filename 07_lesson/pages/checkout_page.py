from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (
            By.CLASS_NAME,
            "summary_info_label.summary_total_label",
        )

    def fill_form(self, first_name, last_name, postal_code):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(
            self.first_name_field)).send_keys(first_name)
        wait.until(EC.presence_of_element_located(
            self.last_name_field)).send_keys(last_name)
        wait.until(EC.presence_of_element_located(
            self.postal_code_field)).send_keys(postal_code)
        wait.until(EC.element_to_be_clickable(
            self.continue_button)).click()

    def get_total(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text.split('$')[1]
