from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
# Инициализация драйвера (один раз в начале)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
driver.maximize_window()


def click_dynamic_button():
    """Кликает на кнопку с динамическим ID на странице dynamicid."""
    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Ждем, пока кнопка станет кликабельной, используя XPATH
        # (CSS Selector не подходит, т.к. ID динамический)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable
            ((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
        )

        # Кликаем на кнопку
        button.click()
        print("Клик выполнен")

    except NoSuchElementException:
        print("Ошибка: Кнопка не найдена")
    except TimeoutException:
        print("Ошибка: Кнопка не стала кликабельной в течение 10 секунд")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    click_dynamic_button()
    sleep(5)


driver.quit()
