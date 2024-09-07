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

    def add_item_to_cart(self, by, item_selector):
        try:
            selected_item = self.select_web_element_by(by, item_selector)
            assert selected_item.is_displayed(), f"Item selected by {by} with selector {item_selector} is not displayed"
            logger.info(f"Adding selected item {by} with selector {item_selector}")
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
        try:
            shopping_cart_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.cart_badge_class))
            )
            number_of_items_in_cart = float(shopping_cart_element.text.replace('$', ''))
            logger.info(f"The shopping cart has {number_of_items_in_cart} items")
            return number_of_items_in_cart
        except TimeoutException:
            # TODO: check the cart image exists, only then return 0
            logger.info(f"Shooping cart is empty")
            return 0