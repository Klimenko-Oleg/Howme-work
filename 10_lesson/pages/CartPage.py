from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class CartPage:
    """
    Класс страницы с корзиной
    """

    def __init__(self, driver: WebDriver) -> None:  # Заменили init на __init__
        self.driver = driver
        self.checkout_button = (
            By.CSS_SELECTOR,
            "[data-test='checkout']"
        )  # Используем data-test

    @allure.step("нажатие на кнопку checkout")
    def checkout(self) -> None:
        """
        Функция для нажатия кнопки checkout
        """
        try:
            wait = WebDriverWait(self.driver, 20)
            checkout_button = wait.until(
                EC.element_to_be_clickable(self.checkout_button)
            )
            checkout_button.click()
        except Exception as e:
            print(f"Не удалось найти или нажать элемент checkout: {e}")
            raise  # Перебросить исключение, чтобы тест не прошел
