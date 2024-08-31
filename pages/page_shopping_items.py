from __future__ import annotations
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    InvalidElementStateException,
    WebDriverException
)
from selenium.webdriver.support import expected_conditions as EC

import logging

import pages.page_base

logger = logging.getLogger(__name__)
current_number_in_cart = 0
class PageCart(pages.page_base.PageBase):
    def __init__(self, browser):
        super().__init__(browser=browser)
        self.cart_badge_class = "shopping_cart_badge"
        self.current_number_in_cart = 0

    def add_item_to_cart(self, by, item_selector):
        try:
            selected_item = self.select_web_element_by(by, item_selector)
            assert selected_item.is_displayed(), f"Item selected by {by} with selector {item_selector} is not displayed"
            selected_item.click()
        except ElementClickInterceptedException as e:
            #  element is not clickable at the point it is clicked.
            logger.error(f"Element click intercepted for {selected_item.Name}. Exception: {e}")
        except ElementNotInteractableException as e:
            # Item exists but not Interactable
            logger.error(f"Element not interactable for {selected_item.Name}. Exception: {e}")
        except NoSuchElementException as e:
            # Item couldn't be found
            logger.error(f"No such element found with {selected_item.Name}. Exception: {e}")
        except StaleElementReferenceException as e:
            #  element is no longer attached to the DOM. the DOM has been updated or refreshed
            logger.error(f"Stale element reference for {selected_item.Name}. Exception: {e}")
        except TimeoutException as e:
            # command takes too long to execute. exceeds waiting for an element to become clickable or visible.
            logger.error(f"Timeout while waiting for element {selected_item.Name} to be clickable. Exception: {e}")
        except InvalidElementStateException as e:
            # Invalid for interaction. like disabled button
            logger.error(f"Invalid element state for {selected_item.Name}. Exception: {e}")
        except WebDriverException as e:
            # webDriver related issues
            logger.error(f"WebDriverException occurred for {selected_item.Name}. Exception: {e}")
        except Exception as e:
            # Any other issue
            logger.error(f"An unexpected error occurred: {e}")

    def get_cart_count(self):
        shopping_cart_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.cart_badge_class))
        )
        number_of_items_in_cart = float(shopping_cart_element.text.replace('$', ''))
        logger.debug(f"The shopping cart has {number_of_items_in_cart} items")
        print("-----------------> ", number_of_items_in_cart)
        return 0#number_of_items_in_cart

if __file__ == "__main__":
    import pytest
    print("---------> running")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.common.by import By
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Initialize WebDriver. replace browser with desired one.
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    # driver.find_element(By.ID, "user-name").clear()  # example of clearing the text field
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 5)
    print("----------->")
    cart_page = PageCart(driver)
    cart_page.add_item_to_cart(By.XPATH, "//div[a[div[contains(text(), 'Fleece')]]]/following-sibling::div//button[contains(@class, 'btn btn_primary btn_small btn_inventory')]")
    print(cart_page.get_cart_count())