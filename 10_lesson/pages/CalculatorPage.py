from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class CalculatorPage:
    """
    Класс для вычислений
    """
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay = '3'
        self.buttons_xpath = {
            '7': '//*[@id="calculator"]/div[2]/span[1]',
            '+': '//*[@id="calculator"]/div[2]/span[4]',
            '8': '//*[@id="calculator"]/div[2]/span[2]',
            '=': '//*[@id="calculator"]/div[2]/span[15]'
        }
        self.result = '15'

    @allure.step("открывает страницу CalculatorPage")
    def open(self) -> None:
        """
        Функция для открытия страницы с калькулятором
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    @allure.step("устанавливает длительность ожидания")
    def set_delay(self) -> None:
        """
        Функция для установки ожидания
        """
        with allure.step("находит элемент delay"):
            calc = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        with allure.step("очищает поле delay"):
            calc.clear()
        with allure.step("заполняет поле delay"):
            calc.send_keys(self.delay)

    @allure.step("производит вычисление")
    def do_calc(self) -> None:
        """
        Фунция нажимает последовательно на следующие кнопки: 7 + 8 =
        """
        with allure.step("нажимает на кнопку 7"):
            self.driver.find_element(
                By.XPATH, self.buttons_xpath.get('7')).click()

        with allure.step("нажимает на кнопку +"):
            self.driver.find_element(
                By.XPATH, self.buttons_xpath.get('+')).click()

        with allure.step("нажимает на кнопку 8"):
            self.driver.find_element(
                By.XPATH, self.buttons_xpath.get('8')).click()

        with allure.step("нажимает на кнопку ="):
            self.driver.find_element(
                By.XPATH, self.buttons_xpath.get('=')).click()

    @allure.step("проверяет результат")
    def expected_result(self) -> bool:
        """
        Функция проверяет результат вычисления калькулятора
        """
        with allure.step("ожидает появление резельтата"):
            waiter = WebDriverWait(self.driver, self.delay)
            waiter.until(
                EC.text_to_be_present_in_element((
                    By.XPATH, '//*[@id="calculator"]/div[1]/div'), self.result)
            )

        with allure.step("извлекает результат с экрана калькулятора"):
            screen = self.driver.find_element(
                By.XPATH, '//*[@id="calculator"]/div[1]/div')
            screen_text = screen.text

        with allure.step("проверяет ожидаемый результат"):
            if screen_text == self.result:
                return True
            else:
                return False
