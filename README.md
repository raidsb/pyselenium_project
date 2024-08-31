# Test Automation with Selenium
Welcome to my Test Automation with Selenium repo. This project aims to showcase automating web application testing with selenium. 

## Technologies Used
1. Selenium WebDriver: Core framework for interacting with and automating web browsers.
2. Python
3. PyTest: Testing frameworks to structure and execute test cases.
4. Allure: Reporting tools to generate detailed test reports with logs, screenshots, and more.
5. CI/CD Integration: Automate test execution in continuous integration pipelines using tools like Jenkins, GitHub Actions, or GitLab CI.

## Key Features Covered in this project
1. Cross-Browser Testing: Although the current tests are set up to run in the Chrome browser, switching to other browsers is fairly straigtforward. Selenium supports cross-browser testing, which helps ensure your application behaves consistently and is compatible across different browsers.
2. Data-Driven Testing: Data-driven testing allows you to run the same test with different sets of input data, making it easier to test various scenarios. Check out the examples provided in this repo to see how it’s done.
3. Page Object Model (POM): I use the Page Object Model design pattern to make our tests easier to maintain and reduce code duplication. By separating the test scripts from the page-specific elements and actions, we keep our code organized and flexible.
4. Scalability: Our test suite is scalable, meaning you can run the tests on your local machine, integrate them into CI/CD pipelines, or execute them on cloud-based testing platforms like Selenium Grid. This flexibility makes it easy to scale up testing efforts as needed.
5. Integration with Testing Frameworks: the tests integrate smoothly with popular test runner frameworks like PyTest, which helps with organizing test cases, running tests efficiently, and generating reports.
6. Cheatsheet, Best practices: check the cheatsheets and best practices used in this repo.

### selenium features covered
1. setting up driver options
2. initializing a driver with options
3. locating an element by id
4. locating an element by class name
5. locating an element by xpath with attribute
6. locating an element by name
7. locating an element by css_selector
6. wait for expected condition like an element to be displayed/located
7. interacting with an element with click()
8. interacting with an element with sending keys like text to a text field
9. interacting with an element with clearing 
10. Using session scope to keep the page loged in

# Test Automation Best Practices with Selenium
* Use Fixtures in conftest.py to avoid redundant code, improve maintainability and setting up the configurations for all tests
* If you have one website to test, get the site in the fixture. This improves code reusability and maintains a clean separation. example [Open the website in conftest.py](tests/tests_individual_tests/conftest.py#L43)

# 
WebDriverWait(browser, 10) is generally preferred over time.sleep() for explicit waits in Selenium tests.

Here's a breakdown of why:

WebDriverWait:

Conditional waiting: Waits for a specific condition to be met (e.g., element visibility, text presence) before proceeding. This avoids unnecessary delays.
Timeout: The timeout argument specifies the maximum time to wait. If the condition is not met within the timeout, a TimeoutException is raised.
Flexibility: Can be used with various expected conditions, allowing for more precise control over waits.
time.sleep():

Fixed delay: Introduces a fixed delay, regardless of whether the condition is met or not. This can lead to inefficient tests, especially if the condition is met quickly.
Less reliable: Can be flaky, as it doesn't account for dynamic page changes or network latency.
Key advantages of WebDriverWait:

Reliability: Ensures tests wait for the correct elements or conditions before proceeding.
Efficiency: Avoids unnecessary delays, making tests faster.
Flexibility: Can be used with various expected conditions.
When to use time.sleep():

Simple, fixed delays: In rare cases where a fixed delay is truly necessary (e.g., waiting for a specific animation to complete), time.sleep() can be used. However, try to avoid it if possible.
In conclusion, WebDriverWait is the recommended approach for explicit waits in Selenium tests. It provides a more reliable and efficient way to handle dynamic page elements and avoid unnecessary delays.

---
2. **Handle Multiple URLs:**
   - If you need to test websites with different starting URLs, create separate fixtures with unique names or use parameterized tests.

3. **Error Handling:**
   - It's wise to incorporate error handling within the fixture or directly in your test to handle potential issues like network errors or invalid URLs. Here's an example with exception handling:

   ```python
   def test_login_functionality(browser):
       try:
           # Test steps using browser
       except Exception as e:
           logger.error(f"Website opening failed: {e}")
       # ... (rest of your test)
   ```

4. **Leverage Page Object Model (POM):**
   - For larger web applications, consider using the Page Object Model (POM) to create separate classes encapsulating page elements and interactions. This promotes maintainability and reduces code duplication.


**In Conclusion:**

By combining fixtures, error handling, and potentially leveraging POM, you can create a more maintainable and reliable approach for opening websites in your Pytest Selenium tests. Remember to tailor the approach to your specific project's needs.

--- 
A Comprehensive Selenium Python Project Structure
Based on the provided information and best practices, here's a recommended project structure:

project_name/
├── requirements.txt
├── .gitignore
├── tests/
│   ├── conftest.py
│   ├── pages/
│   │   ├── login_page.py
│   │   └── home_page.py
│   ├── utils/
│   │   └── wait_utils.py
│   └── test_login.py
├── src/
│   ├── pages/
│   │   ├── login_page.py
│   │   └── home_page.py
│   ├── utils/
│   │   └── wait_utils.py
├── reports/
└── config.ini
Explanation:

requirements.txt: Lists project dependencies (selenium, pytest, etc.).
.gitignore: Specifies files and directories to be ignored by Git.
tests: Contains test cases and supporting files.
conftest.py: For pytest configuration (fixtures, hooks).
pages: Contains page object classes for representing web pages.
utils: Contains utility functions for common tasks (wait helpers, etc.).
test_login.py: An example test case for login functionality.
src: Contains production code (optional, for larger projects).
pages: Can be shared between tests and production code (if applicable).
utils: Utility functions that can be reused in both tests and production.
reports: For storing test reports (e.g., generated by pytest-html).
config.ini: For storing configuration settings (optional).
Key points:

Separation of concerns: Clearly defined folders for tests, source code, and configuration.
Page Object Model (POM): Using page objects for better test maintainability.
Test utilities: Centralizing common test functions in utils folder.
Configuration management: Using a configuration file for test environment settings.
Reporting: Providing a dedicated folder for test reports.
Additional considerations:

Version control: Use Git for effective collaboration and tracking changes.
Virtual environments: Isolate project dependencies using venv or virtualenv.
Continuous integration (CI): Set up CI pipelines for automated testing and deployment.
By following this structure, you'll create a well-organized and maintainable Selenium Python project.


--- using fixtures 
In the context of Selenium Python projects using pytest as the testing framework, conftest.py is a crucial file that serves multiple purposes:

1. Sharing Fixtures:

A fixture is a function that helps to set up and tear down resources needed for tests.
By defining fixtures in conftest.py, you can make them available to any test file within a specific directory or subdirectories. This promotes code reuse and avoids code duplication across tests.
2. Customizing Test Execution:

conftest.py allows you to configure pytest behavior for the entire project or specific directories.
You can define hooks like pytest_runtest_setup and pytest_runtest_teardown to execute arbitrary code before and after each test case.
3. Global Variables and Settings:

While not generally recommended, you can use conftest.py to define global variables or settings that might be shared across multiple tests. However, exercise caution and prefer fixtures for test-specific setup/teardown logic.
Overall Benefits of conftest.py:

Improved Code Readability: Organizes test setup and configuration logic in a central location.
Reduced Code Duplication: Eliminates the need to define common fixtures in every test file.
Enhanced Test Maintainability: Easier to change or update test configuration in a single place.
Here's an example of how you might use conftest.py:

Any test file within the same directory or subdirectory can leverage this fixture without needing to create a new WebDriver instance.
By effectively utilizing conftest.py, you can streamline your Selenium testing process in Python projects.


---------------- 
Fixing these items will indeed improve the quality and robustness of your Selenium test, but to demonstrate an advanced level of using Selenium, consider incorporating additional best practices and techniques. Advanced usage of Selenium often involves not just fixing syntax errors or improving readability but also demonstrating efficiency, maintainability, robustness, and a deeper understanding of the testing framework.

Here are some advanced practices you can integrate into your test to show a more advanced level of using Selenium:

### 1. **Use of Page Object Model (POM)**
The Page Object Model is a design pattern that enhances test maintenance and reduces code duplication. In POM, you create a class for each page of your application and encapsulate the elements and actions related to that page.

**Example**:

Create a `Page` class:

```python
class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.item_with_fleece_selector = "//div[a[div[contains(text(), 'Fleece')]]]/following-sibling::div//button[contains(@class, 'btn btn_primary btn_small btn_inventory')]"
        self.item_swag_selector = "button[name='add-to-cart-sauce-labs-backpack']"
        self.item_tshirt_selector = "button[name='add-to-cart-sauce-labs-bolt-t-shirt']"
        self.cart_badge_class = "shopping_cart_badge"

    def add_item_to_cart(self, item_selector):
        item = self.browser.find_element(By.XPATH, item_selector)
        assert item.is_displayed(), f"Item with selector {item_selector} is not displayed"
        item.click()

    def get_cart_count(self):
        shopping_cart_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.cart_badge_class))
        )
        return int(shopping_cart_element.text)
```

Update the test to use the `CartPage` class:

```python
def test_adding_to_cart(self, browser, login):
    cart_page = CartPage(browser)

    # Add items to the cart
    cart_page.add_item_to_cart(cart_page.item_with_fleece_selector)
    cart_page.add_item_to_cart(cart_page.item_swag_selector)
    cart_page.add_item_to_cart(cart_page.item_tshirt_selector)

    # Assert the cart count
    assert cart_page.get_cart_count() == 3, "Shopping cart does not have the expected number of items"
```

### 2. **Implementing Data-Driven Testing**
Instead of hardcoding item selectors, use a data-driven approach to pass different inputs. This allows for testing different scenarios without changing the test logic.

**Example**:

```python
import pytest

@pytest.mark.parametrize("item_selector", [
    "//div[a[div[contains(text(), 'Fleece')]]]/following-sibling::div//button[contains(@class, 'btn btn_primary btn_small btn_inventory')]",
    "button[name='add-to-cart-sauce-labs-backpack']",
    "button[name='add-to-cart-sauce-labs-bolt-t-shirt']"
])
def test_add_item_to_cart(self, browser, login, item_selector):
    cart_page = CartPage(browser)
    cart_page.add_item_to_cart(item_selector)
    assert cart_page.get_cart_count() == 1, "Item not added to the cart correctly"
```

### 3. **Use of Explicit Waits Effectively**
Avoid using `time.sleep()` and instead use explicit waits where necessary to wait for specific conditions. This makes your tests more reliable and faster.

```python
# Already using WebDriverWait in your example, which is good!
shopping_cart_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)
```

### 4. **Error Handling and Logging**
Implement proper error handling to gracefully deal with unexpected behavior. Additionally, use logging to record the progress of tests and any failures.

**Example**:

```python
import logging

logger = logging.getLogger(__name__)

def test_adding_to_cart(self, browser, login):
    try:
        cart_page = CartPage(browser)

        cart_page.add_item_to_cart(cart_page.item_with_fleece_selector)
        cart_page.add_item_to_cart(cart_page.item_swag_selector)
        cart_page.add_item_to_cart(cart_page.item_tshirt_selector)

        assert cart_page.get_cart_count() == 3, "Shopping cart does not have the expected number of items"
        logger.info("Test passed: 3 items were successfully added to the cart.")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise
```

### 5. **Browser Interactions and Cleanup**
Using advanced interactions such as hovering, drag-and-drop, or dealing with complex JavaScript elements shows deeper knowledge. Also, ensure proper cleanup after tests to reset the state.

**Example**:

```python
from selenium.webdriver.common.action_chains import ActionChains

# Example of using hover action
def test_hover_add_to_cart(self, browser, login):
    cart_page = CartPage(browser)
    item = browser.find_element(By.XPATH, cart_page.item_with_fleece_selector)
    hover = ActionChains(browser).move_to_element(item)
    hover.perform()
    cart_page.add_item_to_cart(cart_page.item_with_fleece_selector)
    assert cart_page.get_cart_count() == 1, "Item not added to cart after hover"
```

### 6. **Headless Browser Testing**
Using a headless browser can speed up tests and is useful for CI/CD environments.

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
```

### Summary

- **Use Page Object Model (POM)**: Improves test organization and maintenance.
- **Data-Driven Testing**: Test multiple scenarios with different data sets.
- **Explicit Waits**: Make tests more reliable by waiting for specific conditions.
- **Error Handling and Logging**: Provide meaningful error messages and logs.
- **Advanced Interactions**: Show knowledge of complex interactions (hover, drag-and-drop).
- **Headless Browser Testing**: Optimize for speed and CI/CD environments.

By integrating these advanced practices, your use of Selenium will not only be more effective but also demonstrate a deep understanding of web automation testing and software quality assurance.

---

To effectively use the Page Object Model (POM) pattern, it's important to organize your code structure in a way that makes it scalable, maintainable, and easy to understand. Here's a typical project structure and how you can organize the page classes:

### Typical Project Structure for Selenium with POM

1. **Project Root Directory**: This is the main directory for your Selenium test project.
2. **`tests/` Directory**: Contains all the test cases.
3. **`pages/` Directory**: Contains all the page object classes.
4. **`conftest.py` or `utils/` Directory**: Contains shared fixtures, utilities, and configuration files.

### Example Project Structure

```
selenium_test_project/
│
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_login.py
│   └── test_checkout.py
│
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── login_page.py
│   └── checkout_page.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

### Implementing the Page Class

- **Directory**: `pages/` – This directory is where all page-related classes will reside.
- **Module**: `cart_page.py` – Each class typically corresponds to a single page or a part of a page in the application.

**Example of `cart_page.py` in the `pages/` directory:**

```python
# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.item_with_fleece_selector = "//div[a[div[contains(text(), 'Fleece')]]]/following-sibling::div//button[contains(@class, 'btn btn_primary btn_small btn_inventory')]"
        self.item_swag_selector = "button[name='add-to-cart-sauce-labs-backpack']"
        self.item_tshirt_selector = "button[name='add-to-cart-sauce-labs-bolt-t-shirt']"
        self.cart_badge_class = "shopping_cart_badge"

    def add_item_to_cart(self, item_selector):
        item = self.browser.find_element(By.XPATH, item_selector)
        assert item.is_displayed(), f"Item with selector {item_selector} is not displayed"
        item.click()

    def get_cart_count(self):
        shopping_cart_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.cart_badge_class))
        )
        return int(shopping_cart_element.text)
```

### Using the Page Class in Your Test

You can use the `CartPage` class in your test cases by importing it. This keeps the test scripts clean and focused on test logic rather than directly interacting with web elements.

**Example of `test_add_to_cart.py` in the `tests/` directory:**

```python
# tests/test_add_to_cart.py

import pytest
from pages.cart_page import CartPage  # Import the CartPage class

def test_adding_to_cart(browser, login):
    cart_page = CartPage(browser)

    # Use methods from CartPage to interact with the page
    cart_page.add_item_to_cart(cart_page.item_with_fleece_selector)
    cart_page.add_item_to_cart(cart_page.item_swag_selector)
    cart_page.add_item_to_cart(cart_page.item_tshirt_selector)

    assert cart_page.get_cart_count() == 3, "Shopping cart does not have the expected number of items"
```

### Explanation

1. **Modularization**: Placing page classes in a dedicated `pages/` directory allows for better organization and reuse of code. Each page class represents a different page or component of the application.

2. **Encapsulation**: Methods within the page class encapsulate interactions and element locators related to that page. This abstraction makes the test scripts cleaner and easier to read.

3. **Scalability**: As the application grows, you can easily add new page classes for new pages or components. It also makes it easy to update locators or methods if the UI changes, as they are centralized in the page classes.

### Best Practices

- **Keep Page Classes Simple**: Each page class should only contain methods relevant to that page. Avoid adding complex logic; focus on interactions with the page elements.
- **Reuse Common Methods**: If multiple pages share common interactions, consider creating a base page class with common methods and inheriting it in your specific page classes.
- **Consistent Naming**: Follow a consistent naming convention for page classes, methods, and selectors. This makes the code easier to understand and maintain.

By organizing your project in this manner and using the Page Object Model, you'll demonstrate advanced-level use of Selenium, showcasing your ability to create maintainable and scalable automated test suites.

------


The decision to place the `tests` and `pages` directories inside or outside the `src` folder depends on the project's structure and conventions, but there are some best practices that can guide you. Below are considerations for both approaches:

### 1. **Tests and Pages Inside the `src` Folder**

- **Pros**:
  - **Encapsulation**: Keeping everything related to the application (including tests) within the `src` folder helps encapsulate the entire application codebase. It keeps all relevant code under one directory, which might be easier to manage.
  - **Logical Grouping**: It can make sense to have all application-related code, including tests and supporting pages, in one place for logical grouping. It shows that the tests are directly related to the source code.

- **Cons**:
  - **Mixing Concerns**: Placing tests alongside source code may mix concerns between production code and test code, potentially leading to confusion about what is deployed versus what is tested.

- **Structure Example**:
    ```
    project_root/
    ├── src/
    │   ├── app/
    │   │   ├── main_code.py
    │   │   └── other_module.py
    │   ├── tests/
    │   │   ├── test_add_to_cart.py
    │   │   └── test_login.py
    │   └── pages/
    │       ├── cart_page.py
    │       └── login_page.py
    ├── conftest.py
    ├── requirements.txt
    └── README.md
    ```

### 2. **Tests and Pages Outside the `src` Folder (Preferred in Many Projects)**

- **Pros**:
  - **Separation of Concerns**: Keeping tests and pages outside of the `src` directory separates the production code from the test code. This makes it clear which parts of the code are for the application itself and which are for testing purposes.
  - **Deployment Clarity**: By keeping tests outside of `src`, there’s no risk of accidentally including test code in production deployments. The `src` folder contains only the code that should go into production.
  - **Standard Practice**: Many modern projects adopt this approach as it aligns with common practices in continuous integration and deployment (CI/CD) pipelines where the `src` directory is the main source code and `tests` are handled separately.

- **Cons**:
  - **More Directories to Manage**: Some might see it as creating more directories, but this is typically outweighed by the benefits of separation.

- **Structure Example**:
    ```
    project_root/
    ├── src/
    │   ├── app/
    │   │   ├── main_code.py
    │   │   └── other_module.py
    ├── tests/
    │   ├── test_add_to_cart.py
    │   ├── test_login.py
    └── pages/
        ├── cart_page.py
        └── login_page.py
    ├── conftest.py
    ├── requirements.txt
    └── README.md
    ```

### Choosing the Right Structure

- **Small Projects**: For smaller projects, having everything inside the `src` folder might not be a big deal and can be convenient.
  
- **Larger or Growing Projects**: As the project grows, maintaining a clear separation between production code and test code becomes more critical. This helps with clarity, maintainability, and managing build and deployment processes.

### Best Practice Recommendation

For most projects, especially those expected to grow, **placing the `tests` and `pages` directories outside the `src` folder** is considered a best practice. This provides clear separation, aligns with common project structures in the industry, and facilitates better management of deployment pipelines.

### Conclusion

While there's flexibility depending on the project's needs and team's preferences, keeping tests and related page objects outside the `src` folder generally provides better organization and clearer separation of concerns, making the codebase easier to understand, maintain, and scale.

---

Using `print` statements in `pytest` tests is generally discouraged because `pytest` provides its own mechanisms for capturing and displaying output. Here’s why you might want to avoid `print` and use `pytest` features instead:

1. **Output Capture**: `pytest` captures output from `print` statements and only displays it if a test fails or if specifically requested with the `-s` option. This behavior can make debugging more difficult if you're relying on `print` statements for visibility into test execution.

2. **Test Reporting**: `pytest` has its own reporting and logging mechanisms that provide structured and more informative output. Using `pytest`'s `assert` statements and logging facilities (e.g., the `logging` module) integrates better with the test framework and reporting.

3. **Test Readability**: Relying on `print` can clutter test output and reduce readability, especially when running a large number of tests. `pytest` asserts and fixtures provide clearer feedback on test results and failures.

Instead of `print`, you can use:

- **Assertions**: Use `assert` statements to validate expected outcomes within your tests.
- **Logging**: Utilize the `logging` module to record debug information, which can be configured to show or hide messages based on severity.

If you need to see output during test execution, run `pytest` with the `-s` flag to disable output capturing:

```bash
pytest -s
```

This will show `print` output in the terminal, but it's generally better to rely on `assert` and `logging` for test-related messages.

--- 
The `docs` folder and the `README.md` file serve different but complementary purposes in a project. Here's a breakdown of each and what content is typically included:

### `README.md`

**Purpose**: The `README.md` file is usually the first point of contact for anyone looking at your project. It provides a quick overview and essential information.

**Typical Content**:
1. **Project Overview**: A brief description of what the project does, its goals, and its main features.
2. **Installation Instructions**: Step-by-step instructions for installing and setting up the project.
3. **Usage**: Basic usage instructions or examples showing how to use the project.
4. **Basic Configuration**: Information on any basic configuration needed to run the project.
5. **Contributing**: Guidelines for contributing to the project, including how to submit issues or pull requests.
6. **License**: A summary of the project's license.
7. **Contact Information**: How to contact the maintainers or developers.

**Characteristics**:
- **Conciseness**: Should be relatively brief and to the point.
- **Accessibility**: Since `README.md` is often displayed on repository home pages (e.g., on GitHub), it should provide a clear and easy-to-follow introduction to the project.
- **General Information**: Focuses on information useful to both users and potential contributors, providing a high-level overview.

### `docs` Folder

**Purpose**: The `docs` folder is intended for more comprehensive and detailed documentation. It may include both user-oriented and developer-oriented information.

**Typical Content**:

1. **User Guide**: Detailed instructions on how to use the application, including advanced features and troubleshooting.
2. **Developer Guide**: Documentation aimed at developers who want to understand the codebase, contribute to the project, or extend its functionality.
3. **API Documentation**: If the project exposes an API, detailed documentation of the API endpoints, request/response formats, authentication, etc.
4. **Architecture Overview**: High-level descriptions of the project's architecture, including diagrams and explanations of how different components interact.
5. **Codebase Structure**: Information about the project's directory structure, key files, and their purposes.
6. **Configuration Details**: Detailed configuration options, settings, and how they affect the project's behavior.
7. **Contribution Guide**: More detailed information on how to contribute, beyond what's in the `README.md`. This could include code style guidelines, testing instructions, etc.
8. **Changelog**: A record of all significant changes made to the project over time.
9. **Tutorials**: Step-by-step tutorials or how-tos for performing specific tasks within the project.

**Characteristics**:
- **Detailed and Comprehensive**: Unlike the `README.md`, the `docs` folder can contain much more detailed information, covering various aspects of the project in depth.
- **Organized Structure**: Documentation in the `docs` folder is usually organized into sections or chapters, making it easier to navigate and find specific information.
- **Specific Audiences**: Can have separate sections for different audiences (e.g., users vs. developers).

### When to Use Each

- **`README.md`**: This is your project's elevator pitch. Use it to give a clear and concise introduction, helping users quickly understand what the project is about, how to get started, and where to find more information. It's like the front page of a website—welcoming and informative.

- **`docs` Folder**: This is your project's detailed manual. Use it to provide in-depth information, tutorials, developer guides, and anything else that users or developers might need to understand or contribute to the project. It's where they can find answers to specific questions or learn about advanced features.

### Example of How They Work Together

- **`README.md`**: Provides a quick start guide, installation commands, and links to key parts of the `docs` for more detailed information.
  
    ```markdown
    # Project Name

    A brief description of the project.

    ## Installation

    ```bash
    pip install project-name
    ```

    ## Usage

    ```bash
    project-name --help
    ```

    ## Documentation

    For more detailed information, please refer to the [full documentation](docs/index.md).

    ## Contributing

    See [CONTRIBUTING.md](docs/contributing.md) for guidelines.
    ```

- **`docs/` Folder**: Contains multiple markdown or HTML files, each covering different topics, such as:
  
    - `index.md`: Introduction and links to other documentation sections.
    - `installation.md`: Detailed installation instructions, including dependencies and environment setup.
    - `usage.md`: Detailed usage guide, including examples and advanced use cases.
    - `api.md`: Full API documentation.
    - `architecture.md`: Diagrams and explanations of the system's architecture.
    - `contributing.md`: Detailed contributing guidelines.

### Conclusion

Both `README.md` and the `docs` folder are essential parts of a well-documented project. The `README.md` provides a high-level overview and acts as the first point of contact, while the `docs` folder offers a deeper dive into the project for those who need more information, whether they're users or developers. Keeping both well-organized and up-to-date helps ensure that anyone interacting with your project can find the information they need easily.

--- 

====================
Selenium Cheat Sheet
====================
* starting driver instance
```python
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
# the executable_path is optional. it will create a new instance of the browser
```
## find elements
1. find element by ID
```python
browser.find_element(By.ID, "user-name").send_keys("standard_user")
```

## selenium features:
### Navigating pages
* get a url
```python
driver.get('https://example.com')
```
### Waits
* WebDriverWait for an expected condition. for example waiting for the presence of an element
```python
h3_element = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']"))
        )
```
### assertions:
1. element.is_displayed
```python
assert h3_element.is_displayed()
```