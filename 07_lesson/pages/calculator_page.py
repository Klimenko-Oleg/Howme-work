from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_field = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, delay: str):
        delay_input_element = self.driver.find_element(*self.delay_input)
        delay_input_element.clear()
        delay_input_element.send_keys(delay)

    def press_button(self, button_locator: tuple):
        self.driver.find_element(*button_locator).click()

    def get_result(self) -> str:
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.result_field, '15')
        )
        return self.driver.find_element(*self.result_field).text
