from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver() -> WebDriver:
    service = ChromeService()
    driver = webdriver.Chrome(service=service)
    return driver
