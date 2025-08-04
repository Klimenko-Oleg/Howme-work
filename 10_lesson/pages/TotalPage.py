from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class TotalPage:
    """
    Класс проверяет итоговую сумму
    """
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)  # Инициализируем wait здесь

    @allure.step("проверяет итоговую сумму")
    def total_result(self) -> None:
        """
        Функция проверяет итоговую сумму всех товаров заказанных покупателем
        """
        EXPECTED_TOTAL = "$58.29"
        with allure.step("находит значение итоговой суммы на странице"):

            total = self.wait.until(  # Используем wait для поиска элемента
                EC.presence_of_element_located((
                    By.XPATH,
                    '//div[@class="summary_total_label"]'
                ))
            )
            total_text = total.text

        with allure.step(
            f'проверяет, что итоговая сумма равна {EXPECTED_TOTAL}'
        ):
            assert total_text.split()[1] == EXPECTED_TOTAL

        # Закрывать браузер здесь неправильно, это должна делать фикстура
        # with allure.step("закрывает браузер"):
        #    self.driver.close()
