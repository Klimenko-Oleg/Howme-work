import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    service = EdgeService()
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay("45")
    calculator.press_button(calculator.button_7)
    calculator.press_button(calculator.button_plus)
    calculator.press_button(calculator.button_8)
    calculator.press_button(calculator.button_equals)
    result = calculator.get_result()
    assert result == "15"
