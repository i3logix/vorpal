from vorpal import ExtendedWebElement, By
from unittest import mock
import pytest

@pytest.fixture
def default_element_data():
    return {
        'name':'',
        'locator': '',
        'by': By.CSS_SELECTOR
    }

@pytest.fixture
def element_and_drivers():
    driver_mock = mock.MagicMock(name='driver')
    element_mock = mock.MagicMock(name='element')
    driver_mock.driver.find_element.return_value = element_mock
    driver = driver_mock

    return (ExtendedWebElement(driver, '', '', By.CSS_SELECTOR), driver_mock, element_mock)
    

def test_constructor(default_element_data):
    driver = None
    ExtendedWebElement(driver, *default_element_data)

def test_get_element(element_and_drivers):
    e, driver, _ = element_and_drivers
    e.text
    driver.driver.find_element.assert_called_once

def test_element_cached(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.click()
    e.click()
    driver.driver.find_element.assert_called_once
    
    element_mock.click.assert_called()
    assert(len([call for call in element_mock.mock_calls if call == call.click()]) == 2)

def test_set_value(element_and_drivers):
    e, driver, element_mock = element_and_drivers

    e.set_value('a')

    element_mock.clear.assert_called_once
    element_mock.send_keys.assert_called_once_with('a')