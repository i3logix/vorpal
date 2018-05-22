from vorpal import webdriver, Keys, ExtendedWebElement, custom_selenium_driver, BaseHttpEndpoint

def test_driver():
    """
    Test that the custom_selenium_driver works at all
    """
    driver = custom_selenium_driver.CustomSeleniumDriver(webdriver.Chrome())
    driver.driver.get('https://www.google.com')
    assert driver.get_title() == 'Google'
    driver.driver.close()

def test_driver_old():
    """
    Test that the basic selenium webdriver works at all.
    This is for direct comparison to test_driver() to ensure underlying test isn't broken
    """
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    driver.close()

def test_elements():
    """
    Test that the ExtendedWebElement class works at all
    """
    driver = webdriver.Chrome()
    driver.get('http://www.python.org')
    search_field = ExtendedWebElement(driver.find_element_by_name("q"), driver)
    search_field.set_value('pycon')
    search_field.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

def test_http_endpoint():
    """
    Test that the BaseHttpEndpoint class can make a GET to a base url
    """
    github_api_endpoint = BaseHttpEndpoint("https://api.github.com")
    response_body = github_api_endpoint.GET('/').json()
    assert response_body["current_user_url"] == "https://api.github.com/user"


