from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def input_field_operations():
    """Perform input field operations."""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("Sky")
        sleep(5)
        input_field.clear()
        input_field.send_keys("Pro")
        sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    input_field_operations()
