from vorpal import webdriver, Keys, ExtendedWebElement, custom_selenium_driver

def test_driver():
    driver = custom_selenium_driver.CustomSeleniumDriver(webdriver.Chrome())
    driver.driver.get('https://www.google.com')
    assert driver.get_title() == 'Google'
    driver.driver.close()

def test_driver_old():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    driver.close()

def test_elements(): 
    driver = webdriver.Chrome()
    driver.get('http://www.python.org')
    search_field = ExtendedWebElement(driver.find_element_by_name("q"), driver)
    search_field.set_value('pycon')
    search_field.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
