from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv)
driver.maximize_window()

url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)

WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!"))

award_image = driver.find_element(By.ID, "award")

print("Award image loaded:")
print(award_image.get_attribute("src"))

driver.quit()
