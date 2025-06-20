from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv)
driver.maximize_window()

url = "http://uitestingplayground.com/textinput"
driver.get(url)

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "newButtonName"))
)
input_field.send_keys("SkyPro")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "updatingButton"))
)
button.click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)
button_text = button.text
print(button_text)

driver.quit()
