from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from time import sleep

class TestLogin():
    def test_valid_login(self, browser):
        """
        Test successful login

        :param browser: driver passed by conftest.py yield
        """

        # Find element using element's id attribute
        browser.find_element(By.ID, "user-name").clear() # example of clearing the text field
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()
        WebDriverWait(browser, 5)

        text = browser.find_element(By.CLASS_NAME, "title").text

        # Check if login was successful
        assert "products" in text.lower(), "'Products' doesn't appear on page"

    def test_invalid_login(self, browser):
        """
        Test showing error msg on invalid username or password

        :param browser: driver passed by conftest.py yield
        """

        # Find element using element's id attribute
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("bad_password")
        browser.find_element(By.ID, "login-button").click()
        WebDriverWait(browser, 5)

        h3_element = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']"))
        )

        # Check if login was successful
        assert h3_element.is_displayed(), "h3 element is not displayed"

