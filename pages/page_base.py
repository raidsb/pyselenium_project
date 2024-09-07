from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, WebDriverException
import logging

logger = logging.getLogger(__name__)

class PageBase:
    def __init__(self, browser):
        self.browser = browser

    def select_web_element_by(self, by, select_stmt) -> WebElement:
        """
        Select a web element by its name

        :param by: selenium by element locator - by.id, by.name, by.css_selector...
        :param select_stmt: name of the element
        :return: a selenium web element
        """
        try:
            return self.browser.find_element(by, select_stmt)
        except NoSuchElementException as e:
            logger.error(f"Element not found by: {by} with stmt: {select_stmt}. Exception: {e}")
            raise
        except InvalidSelectorException as e:
            logger.error(f"Invalid selector used by {by} with stmt: {select_stmt}. Exception: {e}")
            raise
        except WebDriverException as e:
            logger.error(f"WebDriver exception occurred while selecting by {by} with stmt: {select_stmt}. Exception: {e}")
            raise