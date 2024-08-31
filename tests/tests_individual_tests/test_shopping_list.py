from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from time import sleep

class TestShoppingCart():
    def test_shopping_items(self, browser):
        """
        Test successfully showing sell items

        :param browser: driver passed by conftest.py yield
        """

        # Find element using element's id attribute
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()

        text = WebDriverWait(browser, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "title"))
        )

        # Check if login was successful
        assert "products" in text.text.lower(), "'Products' doesn't appear in page"

        # After successful login, check for sell items
        item_swag = browser.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        item_bike_light = browser.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light")
        item_tshirt = browser.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")

        assert item_swag.is_displayed(), "Swag item is not displayed"
        assert item_tshirt.is_displayed(), "t-shirt item is not displayed"
        assert item_bike_light.is_displayed(), "bike item is not displayed"

    def test_adding_to_cart(self, browser):
        """
        Test successfully adding to cart

        :param browser: driver passed by conftest.py yield
        """

        # Find element using element's id attribute
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()

        text = WebDriverWait(browser, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "title"))
        )

        # Check if login was successful
        assert "products" in text.text.lower(), "'Products' is not displayed in page"

        # After successful login, check for sell items
        item_swag = browser.find_element(By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']")
        item_tshirt = browser.find_element(By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-bolt-t-shirt']")

        assert item_swag.is_displayed(), "Swag item is not displayed"
        assert item_tshirt.is_displayed(), "t-shirt item is not displayed"

        item_swag.click()
        item_tshirt.click()

        shopping_cart_element = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert shopping_cart_element.text == "2", "Expected items in cart is 2"