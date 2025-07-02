import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.webdriver_factory import create_driver


@pytest.fixture()
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_form("John", "Doe", "12345")

    total = checkout_page.get_total()
    assert total == "58.29"
