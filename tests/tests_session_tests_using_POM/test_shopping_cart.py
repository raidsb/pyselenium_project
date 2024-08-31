from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages import page_shopping_items
from pages.page_shopping_items import current_number_in_cart
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

        # Selecting some items
        page_cart = page_shopping_items.PageCart(browser)
        page_cart.add_item_to_cart(by=by, item_selector=select_stmt)
        page_shopping_items.current_number_in_cart +=1
        items_in_cart = page_cart.get_cart_count()
        logger.info(f"items in cart: {items_in_cart}")
        assert items_in_cart == page_cart.current_number_in_cart, f"Expected items in cart is {page_cart.current_number_in_cart}, actual {items_in_cart}"

    def tes1t_add_cheapest_item_in_the_cart(self, browser, login):
        """
        Selecting items from list based on prices

        :param browser:
        :param login:
        :return:
        """

        # Find all price elements
        price_elements = browser.find_elements(By.XPATH, "//div[@class='inventory_item_price']")

        # List of tuples containing price and corresponding button
        add_to_cart_buttons = []

        # Iterate through price elements to find the minimum price
        for price_element in price_elements:
            price_text = price_element.text.replace('$', '')  # Remove the dollar sign
            price = float(price_text)  # Convert to float

            # Find the corresponding "Add to cart" button
            add_to_cart_button = price_element.find_element(By.XPATH,
                                                            "./following-sibling::button")

            item = (price, add_to_cart_button)
            add_to_cart_buttons.append(item)

        # Using list is intentional. plan to use it to select other items based on price
        items_sorted_by_price = sorted(add_to_cart_buttons, key=lambda el: (el[0]))

        items_sorted_by_price[0][1].click()

        shopping_cart_element = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        # There are already added items to the cart
        assert shopping_cart_element.text == "4", "Expected items in cart is 4"
    #
    # def te1st_remove_item_from_cart(self, browser, login):
    #     """
    #     Test removing items from the cart
    #
    #     :param browser: web driver passed by conftest yield
    #     :param login: login session kept valid and passed to each test
    #     :return:
    #     """
    #
    #     # Remove a product from the cart
    #     remove_buttons = browser.find_elements(By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory ' and text()='Remove']")
    #     remove_buttons[0].click()
    #
    #     # Verify that the cart badge is not displayed anymore
    #     cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    #     assert cart_badge.text == '3', "Cart badge not showing the expected number of items in the cart: 1"
    #
    # def te1st_add_items_by_their_order_in_the_list(self, browser, login):
    #     """
    #     Selecting items based on their order in the list of items
    #
    #     :param browser:
    #     :param login:
    #     :return:
    #     """
    #
    #     # selecting items based on their order in the list
    #     # item_first_product = browser.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[last()-1]")
    #     item_last_product = browser.find_element(By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory '])[last()]")
    #     # assert item_first_product.is_displayed()
    #     assert item_last_product.is_displayed()
    #     # item_first_product().click()
    #     item_last_product.click()
    #
    #     shopping_cart_element = WebDriverWait(browser, 10).until(
    #         expected_conditions.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    #     )
    #
    #     # There are already added items to the cart
    #     assert shopping_cart_element.text == "4", "Expected items in cart is 4"