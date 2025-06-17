from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)

try:
    def image_with_src(driver):
        el = driver.find_element(By.ID, "award")
        return el if el.get_attribute("src") else False

    image = WebDriverWait(driver, 15).until(image_with_src)

    print("Изображение загружено:")
    print(image.get_attribute("src"))

except TimeoutException:
    print("Ошибка: изображение не загрузилось вовремя.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
finally:
    driver.quit()
