from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture()
def driver():
    # 1. Настройка браузера
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_shop(driver):
    # 2. Авторизация
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров в корзину
    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for product_id in products:
        driver.find_element(By.ID, product_id).click()

    # 4. Переход в корзину и оформление заказа
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # 5. Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Олег")
    driver.find_element(By.ID, "last-name").send_keys("Клименко")
    driver.find_element(By.ID, "postal-code").send_keys("145117")
    driver.find_element(By.ID, "continue").click()

    total_element = driver.find_element(
        By.CLASS_NAME, "summary_total_label"
    )
    actual_total = total_element.text
    expected_total = "Total: $58.29"

    assert actual_total == expected_total, (
        f"Expected {expected_total}, but got {actual_total}"
    )
