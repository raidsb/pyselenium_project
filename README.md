# Test Automation with Selenium
Welcome to my Test Automation with Selenium repo. This project aims to showcase automating web application testing with selenium. 

## Technologies Used
1. Selenium WebDriver: Core framework for interacting with and automating web browsers.
2. Python
3. PyTest: Testing frameworks to structure and execute test cases.
4. **IN PROGRESS** BDD: Behavioral-Driven-Development using python Behave library
4. **IN PROGRESS** Allure: Reporting tools to generate detailed test reports with logs, screenshots, and more.
5. **IN PROGRESS** Static code analysis: using python linters to sniff any code smell and improve code quality
5. **IN PROGRESS** CI/CD Integration: Automate test execution in continuous integration pipelines using tools like Jenkins, GitHub Actions, or GitLab CI.

## Key Features Covered in this project
1. Cross-Browser Testing: Although the current tests are set up to run in the Chrome browser, switching to other browsers is fairly straigtforward. Selenium supports cross-browser testing, which helps ensure your application behaves consistently and is compatible across different browsers.
2. Data-Driven Testing: Data-driven testing allows you to run the same test with different sets of input data, making it easier to test various scenarios. Check out the examples provided in this repo to see how it’s done.
3. Page Object Model (POM): I use the Page Object Model design pattern to make our tests easier to maintain and reduce code duplication. By separating the test scripts from the page-specific elements and actions, we keep our code organized and flexible.
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

### selenium features to be covered
1. using hover 
2. using drag_and_drop
3. handling javascript

## Test Automation Best Practices
[Test Automation Best Practices](docs/mds/SeleniumBestPractices.md)

## Selenium Cheat Sheet
[Selenium Cheat Sheet](docs/mds/SeleniumCheatSheet.md)

# Continuous Improvement
This repo is on ongoing improvement. 