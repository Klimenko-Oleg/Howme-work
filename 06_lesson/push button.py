from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv)
driver.maximize_window()

url = "http://uitestingplayground.com/ajax"
driver.get(url)

ajax_button = WebDriverWait(driver, 17).until(
    EC.element_to_be_clickable((By.ID, "ajaxButton"))
)
ajax_button.click()

green_label = WebDriverWait(driver, 17).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

text = green_label.text
print(text)
