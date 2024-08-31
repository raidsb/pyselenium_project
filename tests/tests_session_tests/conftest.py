import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time
import logging

# Set up logging
logging.basicConfig(
    filename='pyselenium_project_log.txt',  # Specify the log file name
    filemode='a',  # Append to the file instead of overwriting ('w' for overwrite)
    # Formatting the logging msg: timestamp - severity level - message
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.INFO  # Log level
)
logger = logging.getLogger(__name__)

# @pytest.fixture is a decorator used to define a function that serves as a fixture in pytest.
# Fixtures are responsible for setting up and tearing down resources needed for your tests.
@pytest.fixture(scope="session")
def browser():
    # Setup web driver options
    # option1: run the tests in headless mode. No browser is visible. comment out if no browser is needed
    # option2: disables GPU acceleration. Can be helpful in certain env or for performance optimization.
    # option3: bypasses the OS security model. Can be necessary in some environments, especially when running
    # ChromeDriver inside containers or other isolated environments.
    # option4: Sets the window size of the browser to 1920x1080 pixels. Not used in headless mode.
    # Can be useful if you're running the browser with a visible window.
    # option5: for not prompting DevTools information. just show the browser from user perspective. note: not used with headless mode
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Initialize WebDriver. replace browser with desired one.
    driver = webdriver.Chrome(options=options)

    # Get the website URL to test.
    driver.get("https://www.saucedemo.com/")

    # Explicit wait for the page title to change to "Swag Labs"
    WebDriverWait(driver, 10).until(
        expected_conditions.title_is("Swag Labs")
    )

    # Add some logging information
    logger.info(f"Setting up the browser with options: {driver.name}")

    # Generate a driver for each pytest test function
    yield driver

    # Teardown
    driver.quit()  # Teardown

    logger.info("Tearing down completed")

@pytest.fixture(scope="session")
def login(browser):
    """
    Test successful login and keep the logedin session for the rest of the tests

    :return:
    """

    # Find element using element's id attribute
    browser.find_element(By.ID, "user-name").clear()  # example of clearing the text field
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    WebDriverWait(browser, 5)

    text = browser.find_element(By.CLASS_NAME, "title").text

    # Check if login was successful
    assert "products" in text.lower()

    # or
    # assert "inventory" in driver.current_url