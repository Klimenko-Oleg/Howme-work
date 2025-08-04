import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
def driver():  # Убрали -> WebDriver
    """
    фикстура устанавливает подходящую версию ChromeDriver
    для работы с установленной версией браузера Chrome.
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # установка неявного ожидания в 15 сек
    driver.implicitly_wait(15)

    # автоматизация инициализации веб-драйвера до выполнения теста
    # и его корректное закрытие после завершения теста
    # driver.maximize_window()
    yield driver
    print(driver)
    driver.quit()


@allure.step("тестирует вычисление калькулятора")
@allure.title("калькулятор")
@allure.description(
    "Функция создает объект calculator_page,"
    "открывает страницу calculator_page,"
    "устанавливает паузу, производит расчет, проверяет результат."
 )
@allure.feature("вычисляет")
@allure.severity("critical")
def test_calculator(driver: WebDriver) -> None:
    """
    Функция создает объект calculator_page, открывает стр.,
    устанавливает паузу, производит расчет, проверяет результат.
    """
    with allure.step("создает объект calculator_page"):
        calculator_page = CalculatorPage(driver)
    with allure.step("открывает страницу calculator_page"):
        calculator_page.open()
    with allure.step("устанавливает длительность ожидания"):
        calculator_page.set_delay()
    with allure.step("производит вычисление"):
        calculator_page.do_calc()
    with allure.step("проверяет результат вычисления"):
        assert calculator_page.expected_result()
