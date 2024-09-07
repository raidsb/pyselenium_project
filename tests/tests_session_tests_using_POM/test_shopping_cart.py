from selenium.webdriver.common.by import By
from pages import page_shopping_items
import pytest
import logging

logger = logging.getLogger(__name__)

class TestShoppingCart:
    @pytest.mark.parametrize("by, select_stmt", [
        (By.XPATH, "//div[a[div[contains(text(), 'Fleece')]]]/following-sibling::div//button[contains(@class, 'btn btn_primary btn_small btn_inventory')]"),
        (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']"),
        (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-bolt-t-shirt']")
    ])
    def test_adding_to_cart(self, browser, login, by, select_stmt):
        """
        Test successfully adding to cart

        :param browser: driver passed by conftest.py yield
        """

        # Adding item to cart
        page_cart = page_shopping_items.PageCart(browser)
        items_in_cart_before_adding = page_cart.get_cart_count()
        page_cart.add_item_to_cart(by=by, item_selector=select_stmt)
        items_in_cart_after_adding = page_cart.get_cart_count()
        assert items_in_cart_after_adding == items_in_cart_before_adding + 1, f"Expected items in cart is {items_in_cart_before_adding + 1}, actual {items_in_cart_after_adding}"