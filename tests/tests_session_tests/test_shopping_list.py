from selenium.webdriver.common.by import By

class TestShoppingList():
    def test_shopping_items(self, browser, login):
        """
        Test successfully showing sell items

        :param browser: driver passed by conftest.py yield
        """

        # Check three items are listed in the page
        item_swag = browser.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        item_bike_light = browser.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light")
        #item_tshirt = browser.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")

        assert item_swag.is_displayed()
        #assert item_tshirt.is_displayed()
        assert item_bike_light.is_displayed()

    def test_shopping_list_sort_by_price(self, browser, login):
        """
        Test sorting listed items by price

        :param browser:
        :param login:
        :return:
        """

        # Locate the sorting dropdownlist and choose sorting by price option
        sort_dropdown = browser.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//select[@class='product_sort_container']/option[@value='hilo']").click()

        # Verify that the listed products are sorted by price in descending order
        # 1) First get all the items with the class inventory_item_price. all listed items have the same class name
        # 2) Convert all the "text" values from the selected items to float after removing the '$'
        # 3) Assert that values are sorted from High to Low
        prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text.replace('$', '')) for price in prices]
        assert prices == sorted(prices, reverse=True), "Products are not sorted by price in descending order"