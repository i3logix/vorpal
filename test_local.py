from vorpal import webdriver, Keys, ExtendedWebElement, custom_selenium_driver, BaseHttpEndpoint, WebDriverFactory
import pytest
from vorpal import webdriver, Keys, By
import os

@pytest.fixture(scope="module")
def page():
    """
    Return url and title of local test webpage
    Assumes test.html is in current working directory (os.getcwd())
    """
    return {
        'title': 'Vorpal',
        'url': 'file:{}/test.html'.format(os.getcwd())
        }

@pytest.fixture(scope="module")
def driver(page):
    driver_factory = WebDriverFactory('chrome', page['url'])
    driver = driver_factory.get_webdriver_instance()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def selenium_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_driver(driver, page):
    """
    Test that the custom_selenium_driver works at all
    """
    assert driver.title == page['title']

def test_driver_old(selenium_driver, page):
    """
    Test that the basic selenium webdriver works at all.
    This is for direct comparison to test_driver() to ensure underlying test isn't broken
    """
    selenium_driver.get(page['url'])
    assert selenium_driver.title == page['title']

def test_element(driver, page):
    """
    Test that the ExtendedWebElement class works at all
    """
    driver.get(page['url'])
    h1 = ExtendedWebElement(driver, 'test h1', 'test-h1', By.ID)
    assert(h1.text == 'Test H1')

def test_customwebdriver_get_element(driver):
    """
    Test that our custom webdriver class returns working extendedweblement from get_element
    """
    h1 = driver.get_element({'Element name': 'Test H1', 'locator_type': 'id', 'locator': 'test-h1'})
    assert(h1.text == 'Test H1')

def test_customwebdriver_get_elements(driver):
    """
    Test that our custom webdriver class returns list of working extendedweblements from get_elements
    """
    li_list = driver.get_elements({
        'Element name': 'List items',
        'locator_type': 'css_selector',
        'locator': 'li'
        })
    assert li_list[0].text == 'li-1'
    assert li_list[1].text == 'li-2'

def test_customwebdriver_find_element(driver):
    """
    Test that our custom webdriver class returns working extendedweblement from find_element
    """
    h1 = driver.find_element(By.ID, 'test-h1')
    assert(h1.text == 'Test H1')

def test_customwebdriver_find_elements(driver):
    """
    Test that our custom webdriver class returns list of working extendedweblements from find_elements
    """
    li_1 = driver.find_elements(By.CSS_SELECTOR, 'li')[0]
    assert li_1.text == 'li-1'
