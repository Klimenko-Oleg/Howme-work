from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class MainPage:
    """
    Класс добавления товаров в корзину
    """
    SAUCE_LABS_BACKPACK_ID = "add-to-cart-sauce-labs-backpack"
    SAUCE_LABS_BOLT_T_SHIRT_ID = "add-to-cart-sauce-labs-bolt-t-shirt"
    SAUCE_LABS_ONESIE_ID = "add-to-cart-sauce-labs-onesie"
    CART_XPATH = '//*[@id="shopping_cart_container"]/a'

    def __init__(self, driver: WebDriver) -> None:  # Заменили init на __init__
        self.wait = WebDriverWait(driver, 20)
        self.driver = driver

    @allure.step("добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """
        Функция для добавления товаров в корзину
        """
        with allure.step("добавляет рюкзак в корзину"):
            self.wait.until(
                EC.element_to_be_clickable((
                    By.ID, self.SAUCE_LABS_BACKPACK_ID))).click()

        with allure.step("добавляет футболку в корзину"):
            self.wait.until(
                EC.element_to_be_clickable((
                    By.ID, self.SAUCE_LABS_BOLT_T_SHIRT_ID))).click()

        with allure.step("добавляет детское боди в корзину"):
            self.wait.until(
                EC.element_to_be_clickable((
                    By.ID, self.SAUCE_LABS_ONESIE_ID))).click()

    @allure.step("нажимает на кнопку cart")
    def go_to_cart(self) -> None:
        """
        Функция для перехода в корзину
        """
        self.driver.find_element(By.XPATH, self.CART_XPATH).click()
