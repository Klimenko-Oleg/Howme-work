import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture(scope="function")
def driver():
    service = EdgeService()  # Убрал executable_path, т.к. драйвер в PATH
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
               "data-types.html")

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for id, value in data.items():
        driver.find_element(By.NAME, id).send_keys(value)

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )

    zip_code_class = driver.find_element(By.ID, "zip-code").\
        get_attribute("class")
    assert "alert-danger" in zip_code_class

    for id in data:
        element_class = driver.find_element(By.ID, id).\
            get_attribute("class")
        assert "alert-success" in element_class
