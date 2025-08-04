from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class AuthPage:
    """
    Класс авторизации пользователя
    """

    USERNAME_XPATH = '//*[@id="user-name"]'
    PASSWORD_XPATH = '//*[@id="password"]'
    LOGIN_BUTTON_XPATH = '//*[@id="login-button"]'

    def __init__(self, driver: WebDriver) -> None:  # Заменили init на __init__
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce",
        }

    @allure.step("открытие страницы")
    def open(self) -> None:
        """
        Функция открывает страницу AuthPage
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("заполнение данных пользователя")
    def fill_filds(self) -> None:
        """
        Функция заполняет поля для авторизации
        """
        with allure.step("заполнение поля user-name"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, self.USERNAME_XPATH))).send_keys(
                        self.fields.get('user-name'))

        with allure.step("заполнение поля password"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH, self.PASSWORD_XPATH))).send_keys(
                        self.fields.get('password'))

    @allure.step("нажатие на submit")
    def submit_form(self) -> None:
        """
        Функция для отправки данных авторизации
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, self.LOGIN_BUTTON_XPATH))).click()
