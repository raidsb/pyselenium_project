import pytest
from selenium.webdriver.common.by import By

from time import sleep

class TestLogin():
    def test_valid_login(self, browser):
        """Test successful login"""

        browser.get("https://www.saucedemo.com/")
        sleep(3)

        # Find element using element's id attribute
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()
        sleep(5)

        text = browser.find_element(By.CLASS_NAME, "title").text

        # Check if login was successful
        assert "products" in text.lower()