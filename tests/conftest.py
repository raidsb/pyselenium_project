import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture is a decorator used to define a function that serves as a fixture in pytest.
# Fixtures are responsible for setting up and tearing down resources needed for your tests.
@pytest.fixture
def browser():
    # The setup. Replace with your desired browser.
    # Set options for not prompting DevTools information
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    # Generate a driver for each pytest test function
    yield driver

    # Teardown
    driver.quit()  # Teardown


