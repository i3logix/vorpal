from unittest import mock
import pytest
from vorpal import custom_selenium_driver, By

@pytest.fixture
def driver_and_mock():
    driver_mock = mock.MagicMock()
    d = custom_selenium_driver.CustomSeleniumDriver(driver_mock)
    return d, driver_mock


@pytest.mark.parametrize("by_str,expected", [
    ('id', By.ID),
    ('xpath', By.XPATH),
    ('css_selector', By.CSS_SELECTOR),
    ('name', By.NAME),
    ('link_text', By.LINK_TEXT),
    ('class', By.CLASS_NAME),
    ('ID', By.ID),
])
def test_get_by_type(by_str, expected):
    d = custom_selenium_driver.CustomSeleniumDriver(mock.MagicMock())
    assert(d.get_by_type(by_str) == expected)

def test_take_screen_shot(driver_and_mock):
    d, driver_mock = driver_and_mock
    d.take_screen_shot('test')
    driver_mock.save_screenshot.assert_called_once()

@pytest.mark.parametrize("direction,expected", [
    ('up', 'window.scrollBy(0, -1000);'),
    ('down', 'window.scrollBy(0, 1000);'),
])
def test_scroll_window(driver_and_mock, direction, expected):
    d, driver_mock = driver_and_mock
    d.scroll_window(direction)
    driver_mock.execute_script.assert_called_once_with(expected)



