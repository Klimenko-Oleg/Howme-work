import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from pages.TotalPage import TotalPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
def driver():  # Убрали -> WebDriver
    """
    фикстура устанавливает подходящую версию ChromeDriver
    для работы с установленной версией браузера Chrome.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    print(driver)
    driver.quit()


@allure.step("тестирует интернет магазин")
@allure.title("интернет магазин")
@allure.description(
    "Функция авторизует пользователя, добавляет товары в корзину,"
    "нажимает на кнопку checkout, заполняет данные пользователя,"
    "проверяет итоговую сумму."
 )
@allure.feature("проверяет итоговую сумму")
@allure.severity("critical")
def test_swag_site(driver: WebDriver) -> None:
    """Функция авторизует пользователя, добавляет товары в корзину,
    нажимает на кнопку checkout, заполняет данные пользователя,
    проверяет итоговую сумму.
    """
    with allure.step("создает объект AuthPage"):
        auth_page = AuthPage(driver)
    with allure.step("открывает страницу AuthPage"):
        auth_page.open()
    with allure.step("заполняет поля для авторизации"):
        auth_page.fill_filds()
    with allure.step("нажимает на кнопку submit"):
        auth_page.submit_form()
    with allure.step("создает объект MainPage"):
        main_page = MainPage(driver)
    with allure.step("добавляет товары в карзину"):
        main_page.add_to_cart()
    with allure.step("нажимает на кнопку cart"):
        main_page.go_to_cart()

    with allure.step("создает объект CartPage"):
        cart_page = CartPage(driver)
    with allure.step("нажимает на кнопку checkout"):
        cart_page.checkout()
    with allure.step("создает объект OrderPage"):
        order_page = OrderPage(driver)
    with allure.step("заполняет данные пользователя"):
        order_page.fill_filds()
    with allure.step("нажимает на кнопку continue"):
        order_page.continue_click()
    with allure.step("создает объект TotalPage"):
        total_page = TotalPage(driver)
    with allure.step("проверяет итоговую сумму"):
        total_page.total_result()
