import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function")
def browser():
    """Инициализация и закрытие браузера Edge."""
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.implicitly_wait(5)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )
    yield driver
    driver.quit()


def test_data_types_form(browser):
    """Тест заполнения формы и проверки подсветки полей."""

    first_name = browser.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = browser.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = browser.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone_number = browser.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")

    zip_code = browser.find_element(By.NAME, "zip-code")  # Оставляем пустым

    city = browser.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = browser.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = browser.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = browser.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    # 2. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Функция для проверки цвета поля
    def check_field_color(browser, element, expected_color):
        """Проверяет, что поле имеет ожидаемый цвет."""
        WebDriverWait(browser, 10).until(
            lambda driver: element.value_of_css_property(
                'background-color') != 'rgba(0, 0, 0, 0)'
        )

        color = element.value_of_css_property('background-color')
        if expected_color == "red":
            assert "rgba(248, 215, 218" in color, (
                f"Ожидался красный цвет, получен {color}"
            )
        elif expected_color == "green":
            assert "rgba(229, 243, 217" in color, (
                f"Ожидался зеленый цвет, получен {color}"
            )

    # Проверяем Zip code (должен быть красным)
    zip_code = browser.find_element(By.NAME, "zip-code")
    check_field_color(browser, zip_code, "red")

    # Проверяем остальные поля (должны быть зелеными)
    first_name = browser.find_element(By.NAME, "first-name")
    check_field_color(browser, first_name, "green")
    last_name = browser.find_element(By.NAME, "last-name")
    check_field_color(browser, last_name, "green")
    address = browser.find_element(By.NAME, "address")
    check_field_color(browser, address, "green")
    email = browser.find_element(By.NAME, "e-mail")
    check_field_color(browser, email, "green")
    phone_number = browser.find_element(By.NAME, "phone")
    check_field_color(browser, phone_number, "green")
    city = browser.find_element(By.NAME, "city")
    check_field_color(browser, city, "green")
    country = browser.find_element(By.NAME, "country")
    check_field_color(browser, country, "green")
    job_position = browser.find_element(By.NAME, "job-position")
    check_field_color(browser, job_position, "green")
    company = browser.find_element(By.NAME, "company")
    check_field_color(browser, company, "green")
