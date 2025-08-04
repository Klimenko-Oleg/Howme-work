from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class OrderPage:
    """
    Класс для оформления заказа
    """
    FIRSTNAME_XPATH = '//input[@id="first-name"]'
    LAST_NAME_XPATH = '//input[@id="last-name"]'
    POST_CODE_XPATH = '//input[@id="postal-code"]'
    BUTTON_CONTINUE_XPATH = '//input[@id="continue"]'

    def __init__(self, driver: WebDriver) -> None:
        self.wait = WebDriverWait(driver, 6)
        self.driver = driver
        self.fields = {
            'first-name': "Адам",
            'last-name': "Захаров",
            'postal-code': "101000"
        }

    @allure.step("заполнение данных пользователя")
    def fill_filds(self) -> None:
        """
        Функция заполняет данные пользователя, для оформления заказа:
        имя, фамилию, почтовый индекс
        """

        with allure.step("заполнение поля first-name"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, self.FIRSTNAME_XPATH))).send_keys(
                        self.fields.get('first-name'))

        with allure.step("заполнение поля last-name"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, self.LAST_NAME_XPATH))).send_keys(
                        self.fields.get('last-name'))

        with allure.step("заполнение поля postal-code"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, self.POST_CODE_XPATH))).send_keys(
                        self.fields.get('postal-code'))

    @allure.step("нажатие на кнопку continue")
    def continue_click(self) -> None:
        """
        функция нажимает на кнопку continue
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, self.BUTTON_CONTINUE_XPATH))).click()
