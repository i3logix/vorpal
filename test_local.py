import pytest
from vorpal import webdriver, Keys
from vorpal import ExtendedWebElement, WebDriverFactory, BaseHttpEndpoint

@pytest.fixture
def driver():
    driver_factory = WebDriverFactory('chrome', 'http://www.python.org')
    driver = driver_factory.get_webdriver_instance()
    yield driver
    driver.close()

@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

def test_driver(driver):
    """
    Test that the custom_selenium_driver works at all
    """
    driver.get('https://www.google.com')
    assert driver.get_title() == 'Google'

def test_driver_old(selenium_driver):
    """
    Test that the basic selenium webdriver works at all.
    This is for direct comparison to test_driver() to ensure underlying test isn't broken
    """
    selenium_driver.get('https://www.google.com')
    assert selenium_driver.title == 'Google'

def test_elements(selenium_driver):
    """
    Test that the ExtendedWebElement class works at all
    """
    selenium_driver.get('http://www.python.org')
    search_field = ExtendedWebElement(selenium_driver.find_element_by_name("q"), selenium_driver)
    search_field.set_value('pycon')
    search_field.send_keys(Keys.RETURN)
    assert "No results found." not in selenium_driver.page_source

def test_customwebdriver_get_element(driver):
    """
    Test that our custom webdriver class returns working extendedweblement from get_element
    """
    driver.get('http://www.python.org')
    search_field = driver.get_element({'Element name': 'Search input', 'locator_type': 'name', 'locator': 'q'})
    search_field.set_value('pycon')
    search_field.send_keys(Keys.RETURN)
    assert "No results found." not in driver.driver.page_source

def test_customwebdriver_get_elements(driver):
    """
    Test that our custom webdriver class returns list of working extendedweblements from get_elements
    """
    driver.get('http://www.python.org')
    search_field = driver.get_elements({'Element name': 'Search input', 'locator_type': 'name', 'locator': 'q'})[0]
    search_field.set_value('pycon')
    search_field.send_keys(Keys.RETURN)
    assert "No results found." not in driver.driver.page_source


def test_http_endpoint():
    """
    Test that the BaseHttpEndpoint class can make a GET to a base url
    """
    github_api_endpoint = BaseHttpEndpoint("https://api.github.com")
    response_body = github_api_endpoint.GET('/').json()
    assert response_body["current_user_url"] == "https://api.github.com/user"


