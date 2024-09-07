
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