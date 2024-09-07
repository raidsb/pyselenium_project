# Test Automation Best Practices with Selenium
* Use Fixtures in conftest.py. helps to set up configurations shared by all tests to avoid redundant code and improve maintainability -> check the conftest.py files in tests directory.
* If you have one website to test, get the site in the fixture. This improves code reusability and maintains a clean separation.
* Handle Multiple URLs: If you need to test websites with different starting URLs, create separate fixtures with unique names or use parameterized tests. 
* Use WebDriverWait(browser, 10) instead of time.sleep(). It is generally preferred over time.sleep() for explicit waits in Selenium tests, Specially when a wait period is required for some elements to appear.
* Use Conditional waiting: It is very common to wait for some condition to be met before proceeding with further actions. For example, element visibility or text presence. This helps to avoid unnecessary delays.
* Setting Timeout in the WebDriverWait: The timeout argument specifies the maximum time to wait. If the condition is not met within the timeout, a TimeoutException is raised.
* Error Handling: It is generally a good practice to use error handling in your code. 
* Leverage Page Object Model (POM): For large web applications, consider using the Page Object Model (POM), A design pattern that enhances maintainability and reduce duplications by creating separate classes that encapsulate page elements and interactions. In POM, you create a class for each page of your application and encapsulate the elements and actions related to that page -> tests/tests_session_tests_POM directory
* Implementing Data-Driven Testing: Instead of hard coding item selectors, use a data-driven approach to pass different inputs. This allows for testing different scenarios without changing the test logic.
* A recommended selenium python project structure:
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