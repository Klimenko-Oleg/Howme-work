from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

driver.maximize_window()


def click_blue_button():
    """Кликает на синюю кнопку на странице classattr."""
    try:

        driver.get("http://uitestingplayground.com/classattr")

        blue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )

        blue_button.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())

        alert = driver.switch_to.alert

        alert.accept()

    except NoSuchElementException:

        print("Ошибка: Синяя кнопка не найдена")
    except TimeoutException:

        print("Ошибка: Alert не появился или кнопка не стала кликабельной")
    except Exception as e:

        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    click_blue_button()
sleep(5)
driver.quit()
